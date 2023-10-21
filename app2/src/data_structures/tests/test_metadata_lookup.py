import pytest

from app.src.data_structures.object_lookup.metadata_lookup import AttractionMetadataLookup


@pytest.fixture(scope="module")
def attraction_lookup() -> AttractionMetadataLookup:
    return AttractionMetadataLookup()


def test_attraction_lookup_by_id_with_match(attraction_lookup: AttractionMetadataLookup):
    attraction = attraction_lookup.get_attraction_by_id("353347", "330339")
    assert attraction == {"id": "353347", "name": "Haunted Mansion", "park": "DLR", "facility_id": "330339"}


def test_attraction_lookup_by_id_without_match(attraction_lookup: AttractionMetadataLookup):
    attraction = attraction_lookup.get_attraction_by_id("353347_NOT_FOUND", "NONE")
    assert attraction is None
