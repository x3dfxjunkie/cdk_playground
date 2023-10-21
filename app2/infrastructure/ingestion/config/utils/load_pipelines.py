import os
import yaml
from typing import Set, List, Dict, Any
from app.src.ingestion.event_pipes.utils.merge_config import (
    merge_configurations,
    load_and_render_base_template,
    extend_dms_tasks,
)
from app.infrastructure.ingestion.ingestion import IngestionPattern

EXCLUSIONS = (
    "base",
    "appflow",
    "local",
)  # directories in the pipeline configuration we don't want to retrieve files from

CONFIG_DIR = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"


def in_exclusions(file_root: str) -> bool:
    return any(exclusion in file_root for exclusion in EXCLUSIONS)


def aggregate_all_pipeline_configurations(path: str) -> Set[str]:
    return {
        f"{root}/{file}"
        for root, _, files in os.walk(path)
        for file in files
        if file.endswith("yaml") and not in_exclusions(root)
    }


def retrieve_pipeline_configurations(pipeline_configuration_files: Set[str], pattern: str) -> List[Dict[str, Any]]:
    all_pipeline_configurations = []
    for pipeline_configuration_file in pipeline_configuration_files:
        with open(pipeline_configuration_file, "r", encoding="utf-8") as fp:
            pipeline_configuration = yaml.unsafe_load(fp.read())
            if pipeline_configuration.get("ingest_pattern", None) == pattern:
                all_pipeline_configurations.append(pipeline_configuration)
    return all_pipeline_configurations


def load_configurations(ingest_pattern: str):
    aggregated_configurations = aggregate_all_pipeline_configurations(f"{CONFIG_DIR}/pipelines")
    pipeline_configurations = retrieve_pipeline_configurations(aggregated_configurations, ingest_pattern)
    all_configs = []
    for pipeline_config in pipeline_configurations:
        base_config = load_and_render_base_template(CONFIG_DIR, pipeline_config.get("stack_extension"), ingest_pattern)
        config = merge_configurations(base_config, pipeline_config)
        if ingest_pattern == IngestionPattern.DMS:
            config = extend_dms_tasks(base_config, config)
        all_configs.append(config)
    return all_configs
