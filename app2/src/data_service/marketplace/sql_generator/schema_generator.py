import os
from datetime import datetime
from pathlib import Path
from typing import Union
from app.src.data_service.marketplace.sql_generator.helpers import (
    render_sql_template,
    write_sql_file,
    create_folders_tree,
    unblobbing_schema_name,
    sql_section_header,
    load_schema_gen_conf,
)


def generate_schema_sql_files(unique_schemas: set, enviroment_path: Union[Path, str], environment_name: str) -> None:
    schema_generated_sql_directory = os.path.join(enviroment_path, "schemas")
    create_folders_tree(schema_generated_sql_directory)
    static_values = vars(load_schema_gen_conf())
    all_ddls = ""
    for schema_name in unique_schemas:
        ddl = sql_section_header(f"LANDING SCHEMA FOR: {schema_name.upper()} | {datetime.now()}")

        # Landing Schemas:
        ddl += generate_schema_sql_file(
            environment_name=environment_name,
            database_name=f"{environment_name.upper()}_LANDING",
            schema_name=schema_name,
            comments=f'Landing layer schema for {schema_name.replace("LND_", "")}',
            static_values=static_values,
        )

        # Bronze Schemas:
        bronze_schema_name = unblobbing_schema_name(schema_name)
        ddl += sql_section_header(f"BRONZE SCHEMA FOR: {bronze_schema_name.upper()} | {datetime.now()}")
        ddl += (
            generate_schema_sql_file(
                environment_name=environment_name,
                database_name=f"{environment_name.upper()}_DATAHUB",
                schema_name=bronze_schema_name,
                comments=f'Bronze layer schema for {bronze_schema_name.replace("BRZ_", "")}',
                static_values=static_values,
            )
            + "\n\n"
        )

        all_ddls += ddl

        write_sql_file(
            generated_sql_directory=schema_generated_sql_directory,
            file_name=f"{schema_name.lower().split('_',1)[1]}.sql",
            sql=ddl,
        )

    write_sql_file(
        generated_sql_directory=schema_generated_sql_directory,
        file_name="_AllSchemas.sql",
        sql=all_ddls,
    )


def generate_schema_sql(
    environment_name: str, database_name: str, schema_name: str, comments: str, static_values: dict
) -> str:
    return render_sql_template(
        template_name="create_schema.sql",
        environment_name=environment_name,
        database_name=database_name,
        schema_name=schema_name,
        comments=comments,
        **static_values,
    )


def generate_schema_sql_file(
    environment_name: str, database_name: str, schema_name: str, comments: str = "", static_values: dict = None
) -> str:
    return generate_schema_sql(
        environment_name=environment_name,
        database_name=database_name,
        schema_name=schema_name,
        comments=comments,
        static_values=static_values,
    )
