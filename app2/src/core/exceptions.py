"""All exceptions that have to do with Core
"""


class UnsupportedProcessingObjectException(Exception):
    def __init__(self, class_name):
        self.class_name = class_name
        message = f"Unsupported processing object {self.class_name}"
        super().__init__(message)


class UnspecifiedKinesisStreamException(Exception):
    def __init__(self):
        message = "Kinesis stream name not specified."
        super().__init__(message)


class SourceClassSourceName(Exception):
    def __init__(self):
        message = "Source class contains no source_name"
        super().__init__(message)


class SourceNotClass(Exception):
    def __init__(self):
        message = "Source is not a class"
        super().__init__(message)


class SourceClassNotSpecified(Exception):
    def __init__(self):
        message = "Source not specified"
        super().__init__(message)


class GraphValidationException(Exception):
    def __init__(self):
        message = "Graph validation failed."
        super().__init__(message)


class MappedAttributeNotFound(Exception):
    def __init__(self, source_attribute_name):
        message = f"Mapped attribute {source_attribute_name} not found in any sources."
        super().__init__(message)
