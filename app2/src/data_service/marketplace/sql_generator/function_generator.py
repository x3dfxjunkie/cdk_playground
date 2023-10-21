import os
from pathlib import Path
from typing import Union
from app.src.data_service.marketplace.sql_generator.helpers import (
    render_sql_template,
    write_sql_file,
    create_folders_tree,
)


def generate_sql_function(template_name: str, enviroment_path: Union[Path, str], file_name: str, **kwargs):
    """Function to render any sql function.

    Args:
        template_name (str): path of the file to be rendered.
        enviroment_path (Union[Path, str]): environment path under the generated_sql folder
        file_name (str): this is the name of the rendered file.
    """
    func_generated_sql_directory = os.path.join(enviroment_path, "functions")
    create_folders_tree(func_generated_sql_directory)
    ddl = render_function_ddl(template_name=template_name, kwargs=kwargs)
    write_sql_file(
        generated_sql_directory=func_generated_sql_directory,
        file_name=f"{file_name.lower()}.sql",
        sql=ddl,
    )


def render_function_ddl(template_name: str, kwargs: dict) -> str:
    return render_sql_template(template_name=template_name, **kwargs)
