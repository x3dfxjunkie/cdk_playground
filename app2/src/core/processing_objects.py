"""
This module is used for organizing core processing objects.
"""
from dataclasses import dataclass
from dataclasses import fields
from dataclasses_json import dataclass_json
from app.src.core.exceptions import *
from typing import List
import inspect
import networkx as nx


class CoreProcessingSource:
    def __init__(self):
        pass


class CoreProcessingEvent:
    def __init__(self):
        pass


class KinesisSource:
    """Decorator to make sure a class is a dataclass, can be instanciated from a json object,
    and has reference to the kinesis source that will generate events.
    """

    def __init__(self, *args):
        self.args = args

    def __call__(self, cls):
        try:
            cls.source_name = self.args[0]
            return dataclass_json(dataclass(cls))
        except Exception as exc:
            raise UnspecifiedKinesisStreamException() from exc


class ProcessingEvent:
    """Decorator to make sure a processing event has a reference to a source that triggers the event."""

    def __init__(self, *args):
        self.args = args

    def __call__(self, cls):

        if len(self.args) != 1:
            raise SourceClassNotSpecified()
        source = self.args[0]
        if not inspect.isclass(source):
            raise SourceNotClass()
        if not hasattr(source, "source_name"):
            raise SourceClassSourceName()
        cls.source = source
        return dataclass(cls)


class MappedAttribute:
    """Attribute which represents a value from a source."""

    def __init__(self, source_attribute_class, source_attribute_name: str):
        self.source_attribute_name = source_attribute_name
        self.source_class_name = source_attribute_class.__name__


class Parser:
    """Class to parse processing objects and create a directed acyclical graph."""

    def __init__(self, processing_objects: List[object]):
        self.sources = {}
        self.events = []
        for processing_object in processing_objects:
            if isinstance(processing_object, CoreProcessingSource):
                self.sources[processing_object.__class__.__name__] = processing_object
            elif isinstance(processing_object, CoreProcessingEvent):
                self.events.append(processing_object)
            else:
                raise UnsupportedProcessingObjectException(processing_object.__class__.__name__)

    def get_sources(self) -> List[CoreProcessingSource]:
        return self.sources.values()

    def get_events(self) -> List[CoreProcessingEvent]:
        return self.events

    def validate(self):
        for event in self.events:
            if self.sources.get(event.source.__name__) is None:
                return False
        return True

    def generate_graph(self) -> nx.DiGraph:
        if not self.validate():
            raise GraphValidationException()
        graph = nx.DiGraph()
        for source in self.sources.values():
            graph.add_node(source.__class__.__name__, node_object=source)
        for event in self.events:
            graph.add_node(event.__class__.__name__, node_object=event)
            graph.add_edge(event.source.__name__, event.__class__.__name__)
        self._validate_mapped_fields(graph)
        return graph

    def _validate_mapped_fields(self, graph: nx.DiGraph):
        for event in self.events:
            for field in fields(event):
                if isinstance(field.default, MappedAttribute):
                    if not self._check_dependencies_for_field(
                        graph, graph.predecessors(event.__class__.__name__), field.default
                    ):
                        raise MappedAttributeNotFound(field.default.source_attribute_name)
        return True

    def _check_dependencies_for_field(self, graph, dependencies, mapped_field):
        for dependency in dependencies:
            if dependency == mapped_field.source_class_name:
                graph_node = graph.nodes[dependency]
                for attribute in fields(graph_node["node_object"]):
                    if attribute.name == mapped_field.source_attribute_name:
                        return True
        return False
