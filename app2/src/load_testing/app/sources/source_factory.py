"""
    Source Factory    
"""
from app.src.load_testing.app.sources.local_source import LocalSource
from app.src.load_testing.app.sources.s3_source import S3Source
from app.src.load_testing.app.sources.source import Source

# config names
CONFIG_BUCKET_NAME = "bucket_name"
CONFIG_BUCKET_PATH = "path"
CONFIG_LOCAL_PATH = "local_path"


# source types
class SourceType:
    SOURCE_TYPE_S3 = "s3"
    SOURCE_TYPE_LOCAL = "local"


# pylint: disable=C0103,W0621,W0612,W0613
class SourceFactory:
    """
    Class that return an instance of a Object Source according to the source_type
    """

    @staticmethod
    def get_source(source_type, **kwargs) -> Source:
        source = None
        match source_type:
            case SourceType.SOURCE_TYPE_S3:
                source = SourceFactory.get_source_s3(**kwargs)
            case SourceType.SOURCE_TYPE_LOCAL:
                source = SourceFactory.get_source_local(**kwargs)
            case _:
                raise NotImplementedError
        return source

    @staticmethod
    def get_source_s3(config, prefix):
        bucket_name = f"{prefix}-{config[CONFIG_BUCKET_NAME]}"
        bucket_path = config[CONFIG_BUCKET_PATH]
        return S3Source(bucket_name, bucket_path)

    @staticmethod
    def get_source_local(config, prefix=None):
        local_path = config[CONFIG_LOCAL_PATH]
        return LocalSource(local_path)
