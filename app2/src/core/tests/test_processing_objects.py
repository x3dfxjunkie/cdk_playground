"""Test suite for the core processing objects
"""
from app.src.core.processing_objects import (
    KinesisSource,
    ProcessingEvent,
    MappedAttribute,
    Parser,
    CoreProcessingSource,
    CoreProcessingEvent,
)
from app.src.core.exceptions import *
from dataclasses import dataclass
import pytest
import networkx as nx


def test_kinesis_source_name_not_specified():
    with pytest.raises(UnspecifiedKinesisStreamException) as e_info:

        @KinesisSource()
        class TestClass:  # pylint: disable=unused-variable
            another_thing: str
            something: str = "something"


def test_kinesis_source_has_required_attributes():
    @KinesisSource("stream_name")
    @dataclass
    class TestClass(CoreProcessingSource):
        another_thing: str
        something: str = "something"

    test_class = TestClass(another_thing="another_thing")
    assert test_class.source_name == "stream_name"
    assert test_class.something == "something"
    assert test_class.another_thing == "another_thing"
    # Confirm the class has ability to get created from json data.
    assert hasattr(test_class, "schema") and callable(getattr(test_class, "schema"))
    assert hasattr(test_class, "from_json") and callable(getattr(test_class, "from_json"))


def test_processing_event_source_not_specified():
    with pytest.raises(SourceClassNotSpecified) as e_info:

        @ProcessingEvent()
        class ConcreteProcessingEvent(CoreProcessingEvent):  # pylint: disable=unused-variable
            test_event_attribute: str


def test_processing_event_source_not_class():
    with pytest.raises(SourceNotClass) as e_info:

        @ProcessingEvent("bad_argument")
        class ConcreteProcessingEvent(CoreProcessingEvent):  # pylint: disable=unused-variable
            test_event_attribute: str


def test_processing_event_source_class_contains_no_source():
    with pytest.raises(SourceClassSourceName) as e_info:

        @ProcessingEvent(TestNoneSourceClass)
        class ConcreteProcessingEvent(CoreProcessingEvent):  # pylint: disable=unused-variable
            test_event_attribute: str


def test_processing_event_source_class_contains_source():
    @ProcessingEvent(TestKinesisSource)
    class ConcreteProcessingEvent(CoreProcessingEvent):  # pylint: disable=unused-variable
        test_event_attribute: str

    assert ConcreteProcessingEvent.source == TestKinesisSource


def test_processing_event_source_mapping():
    @ProcessingEvent(TestKinesisSource)
    class ConcreteProcessingEvent(CoreProcessingEvent):  # pylint: disable=unused-variable
        test_mapped_attribute: MappedAttribute = MappedAttribute(TestKinesisSource, "test_attribute")

    assert ConcreteProcessingEvent.test_mapped_attribute.source_attribute_name == "test_attribute"


def test_parser_unsupported_processing_object():
    with pytest.raises(UnsupportedProcessingObjectException):
        parser = Parser([TestNoneSourceClass(test_attribute="test")])  # pylint: disable=unused-variable


def test_parser_has_source_and_processing_events():
    parser = Parser([TestKinesisSource(test_attribute="test"), TestProcessingEvent(test_attribute="test")])
    assert len(parser.get_sources()) == 1
    assert len(parser.get_events()) == 1


def test_parser_failed_validation_no_source():
    parser = Parser([TestProcessingEvent(test_attribute="test")])
    assert parser.validate() is False


def test_parser_event_with_source_success():
    parser = Parser([TestKinesisSource(test_attribute="test"), TestProcessingEvent(test_attribute="test")])
    assert parser.validate() is True


def test_parser_events_with_sources_one_missing_failed():
    parser = Parser(
        [
            TestKinesisSource(test_attribute="test"),
            TestProcessingEvent(test_attribute="test"),
            TestProcessingEvent2(test_attribute="test"),
        ]
    )
    assert parser.validate() is False


def test_parser_events_with_sources_success():
    parser = Parser(
        [
            TestKinesisSource(test_attribute="test"),
            TestKinesisSource2(test_attribute="test"),
            TestProcessingEvent(test_attribute="test"),
            TestProcessingEvent2(test_attribute="test"),
        ]
    )
    assert parser.validate() is True


def test_parser_generate_graph_raises_validation_exception():
    with pytest.raises(GraphValidationException) as e_info:
        parser = Parser([TestProcessingEvent(test_attribute="test")])
        parser.generate_graph()


def test_parser_generate_graph_source_and_event():
    parser = Parser([TestKinesisSource(test_attribute="test"), TestProcessingEvent(test_attribute="test")])
    graph = parser.generate_graph()
    assert graph.number_of_nodes() == 2
    assert nx.number_weakly_connected_components(graph) == 1


def test_parser_generate_graph_two_sources_and_events():
    parser = Parser(
        [
            TestKinesisSource(test_attribute="test"),
            TestKinesisSource2(test_attribute="test"),
            TestProcessingEvent(test_attribute="test"),
            TestProcessingEvent2(test_attribute="test"),
        ]
    )
    graph = parser.generate_graph()
    assert graph.number_of_nodes() == 4
    assert nx.number_weakly_connected_components(graph) == 2


def test_parser_generate_graph_multiple_events_single_source():
    parser = Parser(
        [
            TestKinesisSource(test_attribute="test"),
            TestProcessingEvent(test_attribute="test"),
            TestProcessingEvent3(test_attribute="test"),
        ]
    )
    graph = parser.generate_graph()
    assert graph.out_degree[TestKinesisSource.__name__] == 2
    assert graph.in_degree[TestKinesisSource.__name__] == 0
    assert graph.out_degree[TestProcessingEvent.__name__] == 0
    assert graph.in_degree[TestProcessingEvent.__name__] == 1
    assert graph.out_degree[TestProcessingEvent3.__name__] == 0
    assert graph.in_degree[TestProcessingEvent3.__name__] == 1


def test_parser_mapped_attribute_not_found():
    with pytest.raises(MappedAttributeNotFound) as e_info:
        parser = Parser([TestKinesisSource(test_attribute="test"), TestProcessingEventBadMapping()])
        parser.generate_graph()


def test_parser_mapped_attribute_found():
    parser = Parser([TestKinesisSource(test_attribute="test"), TestProcessingEventGoodMapping()])
    graph = parser.generate_graph()
    assert nx.number_weakly_connected_components(graph) == 1


def test_parser_mapped_attribute_exists_but_not_in_dependency_path():
    @KinesisSource("stream_1")
    @dataclass
    class TestKinesisSource1(CoreProcessingSource):
        attribute_in_stream_1: str

    @KinesisSource("stream_2")
    @dataclass
    class TestKinesisSource2(CoreProcessingSource):
        attribute_in_stream_2: str

    @ProcessingEvent(TestKinesisSource1)
    @dataclass
    class TestProcessingEventWrongSourceMapping(CoreProcessingEvent):
        test_mapped_attribute: MappedAttribute = MappedAttribute(TestKinesisSource1, "attribute_in_stream_2")

    with pytest.raises(MappedAttributeNotFound) as e_info:
        parser = Parser(
            [
                TestKinesisSource1(attribute_in_stream_1="attribute_in_stream_1"),
                TestKinesisSource2(attribute_in_stream_2="attribute_in_stream_2"),
                TestProcessingEventWrongSourceMapping(),
            ]
        )
        parser.generate_graph()


@KinesisSource("stream_name")
@dataclass
class TestKinesisSource(CoreProcessingSource):
    test_attribute: str
    __test__ = False


@KinesisSource("stream_name_2")
@dataclass
class TestKinesisSource2(CoreProcessingSource):
    test_attribute: str
    __test__ = False


@dataclass
class TestNoneSourceClass:
    test_attribute: str
    __test__ = False


@ProcessingEvent(TestKinesisSource)
@dataclass
class TestProcessingEvent(CoreProcessingEvent):
    test_attribute: str
    __test__ = False


@ProcessingEvent(TestKinesisSource2)
@dataclass
class TestProcessingEvent2(CoreProcessingEvent):
    test_attribute: str
    __test__ = False


@ProcessingEvent(TestKinesisSource)
@dataclass
class TestProcessingEvent3(CoreProcessingEvent):
    test_attribute: str
    __test__ = False


@ProcessingEvent(TestKinesisSource)
@dataclass
class TestProcessingEventBadMapping(CoreProcessingEvent):
    test_mapped_attribute: MappedAttribute = MappedAttribute(TestKinesisSource, "does_not_exist")
    __test__ = False


@ProcessingEvent(TestKinesisSource)
@dataclass
class TestProcessingEventGoodMapping(CoreProcessingEvent):
    test_mapped_attribute: MappedAttribute = MappedAttribute(TestKinesisSource, "test_attribute")
    non_mapped_attribute: str = "not_mapped"
    __test__ = False
