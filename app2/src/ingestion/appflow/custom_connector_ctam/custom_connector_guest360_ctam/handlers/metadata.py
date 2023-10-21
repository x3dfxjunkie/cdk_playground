"""CTAM metadata handler"""
import json
import logging
from typing import List
from app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam.handlers.client import CTAMResponse
from app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam.handlers import validation, ctam
from custom_connector_sdk.lambda_handler import requests, responses
from custom_connector_sdk.connector import context, fields
from custom_connector_sdk.lambda_handler.handlers import MetadataHandler

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

CTAM_SOBJECTS_URL_FORMAT = "{}breeds"
CTAM_SOBJECT_DESCRIBE_URL_FORMAT = "{}breeds"

# CTAM response keys
SOBJECTS_KEY = "Objects"
OBJECT_DESCRIBE_KEY = "objectDescribe"
CHILD_RELATIONSHIPS_KEY = "childRelationships"
HAS_SUBTYPES_KEY = "hasSubtypes"
NAME_KEY = "name"
FIELDS_KEY = "fields"
TYPE_KEY = "type"
LABEL_KEY = "label"
FILTERABLE_KEY = "filterable"
EXTERNAL_ID_KEY = "externalId"
ID_LOOKUP_KEY = "idLookup"
CREATEABLE_KEY = "createable"
UPDATEABLE_KEY = "updateable"
NILLABLE_KEY = "nillable"
DEFAULTED_ON_CREATE_KEY = "defaultedOnCreate"
DEFAULT_VALUE_KEY = "defaultValue"
UNIQUE_KEY = "unique"


def parse_entities(json_string: str) -> List[context.Entity]:
    """Parse JSON response from CTAM query into a list of Entities."""
    parent_object = json.loads(json_string)
    entity_list = []

    if parent_object.get(SOBJECTS_KEY):
        sobjects = parent_object.get(SOBJECTS_KEY)
        for sobject in sobjects:
            entity_list.append(build_entity(sobject))
            LOGGER.info(entity_list)
    elif parent_object.get(OBJECT_DESCRIBE_KEY):
        entity_list.append(build_entity(parent_object.get(OBJECT_DESCRIBE_KEY)))

    return entity_list


def build_entity(field: dict) -> context.Entity:
    """Build Entity from CTAM field."""
    description = field.get(LABEL_KEY)
    has_child_relationships = CHILD_RELATIONSHIPS_KEY in field and len(field.get(CHILD_RELATIONSHIPS_KEY)) != 0
    has_nested_entities = ctam.get_boolean_value(field, HAS_SUBTYPES_KEY) or has_child_relationships
    identifier_id = ctam.get_string_value(field, NAME_KEY)
    LOGGER.info("this is the key id --- %s ----- dict %s", identifier_id, field)
    return context.Entity(
        entity_identifier=ctam.get_string_value(field, NAME_KEY),
        label=description,
        has_nested_entities=has_nested_entities,
        description=description,
        is_writable=field.get(CREATEABLE_KEY),
    )


def parse_entity_definition(json_string: str) -> context.EntityDefinition:
    """Parse JSON response from CTAM query into an entity definition."""
    parent_object = json.loads(json_string)
    field_definitions = []
    entity = build_entity(parent_object)

    if FIELDS_KEY in parent_object:
        field_list = parent_object.get(FIELDS_KEY)
        for field in field_list:
            field_definitions.append(build_field_definition(field))
    return context.EntityDefinition(entity=entity, fields=field_definitions)


def build_field_definition(field: dict) -> context.FieldDefinition:
    """Build FieldDefinition from CTAM field.`"""
    data_type_label = ctam.get_string_value(field, TYPE_KEY)
    data_type = convert_data_type(data_type_label)
    display_name = ctam.get_string_value(field, LABEL_KEY)
    read_operation_property = fields.ReadOperationProperty(
        is_queryable=ctam.get_boolean_value(field, FILTERABLE_KEY), is_retrievable=True
    )

    write_operation_types = set()
    if ctam.get_boolean_value(field, EXTERNAL_ID_KEY):
        write_operation_types.add(responses.WriteOperationType.UPSERT)
    elif ctam.get_boolean_value(field, ID_LOOKUP_KEY):
        write_operation_types.add(responses.WriteOperationType.UPDATE)
        write_operation_types.add(responses.WriteOperationType.UPSERT)
    write_operation_property = fields.WriteOperationProperty(
        is_creatable=ctam.get_boolean_value(field, CREATEABLE_KEY),
        is_updatable=ctam.get_boolean_value(field, UPDATEABLE_KEY),
        is_nullable=ctam.get_boolean_value(field, NILLABLE_KEY),
        is_defaulted_on_create=ctam.get_boolean_value(field, DEFAULTED_ON_CREATE_KEY),
        supported_write_operations=list(write_operation_types),
    )

    return context.FieldDefinition(
        field_name=ctam.get_string_value(field, NAME_KEY),
        data_type=data_type,
        data_type_label=data_type_label,
        label=display_name,
        description=display_name,
        default_value=ctam.get_string_value(field, DEFAULT_VALUE_KEY),
        is_primary_key=ctam.get_boolean_value(field, UNIQUE_KEY),
        read_properties=read_operation_property,
        write_properties=write_operation_property,
    )


def convert_data_type(data_type_name: str):
    data_type_map = {
        "int": fields.FieldDataType.Integer,
        "double": fields.FieldDataType.Double,
        "long": fields.FieldDataType.Long,
        "id": fields.FieldDataType.String,
        "string": fields.FieldDataType.String,
        "textarea": fields.FieldDataType.String,
        "date": fields.FieldDataType.Date,
        "datetime": fields.FieldDataType.DateTime,
        "time": fields.FieldDataType.DateTime,
        "boolean": fields.FieldDataType.Boolean,
    }
    try:
        return data_type_map[data_type_name]
    except KeyError:
        return fields.FieldDataType.Struct


class CTAMMetadataHandler(MetadataHandler):
    """CTAM Metadata handler."""

    def list_entities(self, request: requests.ListEntitiesRequest) -> responses.ListEntitiesResponse:
        error_details = validation.validate_request_connector_context(request)
        if error_details:
            LOGGER.error("ListEntities request failed with %s", str(error_details))
            return responses.ListEntitiesResponse(is_success=False, error_details=error_details)

        # if request.entities_path:
        #     request_uri = ctam.build_ctam_request_uri(connector_context=request.connector_context, url_format=CTAM_SOBJECTS_URL_FORMAT, request_path=request.entities_path)
        # else:
        #     request_uri = ctam.build_ctam_request_uri(connector_context=request.connector_context, url_format=CTAM_SOBJECTS_URL_FORMAT, request_path="")

        # ctam_response = ctam.get_ctam_client(request.connector_context).rest_get(request_uri)
        ctam_response = self.get_ctam_static_entity()

        error_details = ctam.check_for_errors_in_ctam_response(ctam_response)

        if error_details:
            return responses.ListEntitiesResponse(is_success=False, error_details=error_details)
        return responses.ListEntitiesResponse(is_success=True, entities=parse_entities(ctam_response.response))

    def describe_entity(self, request: requests.DescribeEntityRequest) -> responses.DescribeEntityResponse:
        error_details = validation.validate_request_connector_context(request)
        if error_details:
            LOGGER.error("DescribeEntity request failed with %s", str(error_details))
            return responses.DescribeEntityResponse(is_success=False, error_details=error_details)

        # request_uri = ctam.build_ctam_request_uri(connector_context=request.connector_context, url_format=CTAM_SOBJECT_DESCRIBE_URL_FORMAT, request_path=request.entity_identifier)

        # ctam_response = ctam.get_ctam_client(request.connector_context).rest_get(request_uri)
        ctam_response = self.get_ctam_describe_entity("Breeds")
        LOGGER.info(ctam_response)
        error_details = ctam.check_for_errors_in_ctam_response(ctam_response)

        if error_details:
            return responses.DescribeEntityResponse(is_success=False, error_details=error_details)
        return responses.DescribeEntityResponse(
            is_success=True, entity_definition=parse_entity_definition(ctam_response.response)
        )

    def get_ctam_static_entity(self):
        return CTAMResponse(
            status_code=200,
            response="""
                                    {
                                        "Objects": [{
                                                "name": "Title",
                                                "label": "CTAM Title",
                                                "hasNestedEntities": false
                                            }
                                        ]
                                    }
                                  """,
            error_reason="",
        )

    def get_ctam_describe_entity(self, entity_identifier: str):
        entity = {
            "name": "Title",
            "label": "CTAM Title",
            "hasNestedEntities": False,
            "fields": [
                {
                    "type": "int",
                    "name": "TitleID",
                    "unique": True,
                    "label": "Title ID",
                    "filterable": True,
                    "idLookup": "TitleID",
                    "createable": True,
                    "updateable": False,
                    "nillable": False,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "int",
                    "name": "StatusID",
                    "unique": False,
                    "label": "StatusI D",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "int",
                    "name": "TitleTypeID",
                    "unique": False,
                    "label": "Title TypeID",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "int",
                    "name": "TitleFormatID",
                    "unique": False,
                    "label": "Title Format ID",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "TitleAlternateIds",
                    "unique": False,
                    "label": "Local Titles",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "TitleTalents",
                    "unique": False,
                    "label": "Title Talents",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "TitleProductionCompany",
                    "unique": False,
                    "label": "Title Production Company",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "int",
                    "name": "EpisodeNumber",
                    "unique": False,
                    "label": "EpisodeNumber",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "int",
                    "name": "ForeignEpisodeNumber",
                    "unique": False,
                    "label": "Foreign Episode Number",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "TitleRatings",
                    "unique": False,
                    "label": "Title Ratings",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "datatime",
                    "name": "CreateDate",
                    "unique": False,
                    "label": "Create Date",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "CreatorID",
                    "unique": False,
                    "label": "Creator ID",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "UpdatedByID",
                    "unique": False,
                    "label": "Updated By ID",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "OriginalTitleName",
                    "unique": False,
                    "label": "Original Title Name",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "StandardizedTitleName",
                    "unique": False,
                    "label": "Standardized Title Name",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "DisambiguatedTitleName",
                    "unique": False,
                    "label": "Disambiguated Title Name",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "datetime",
                    "name": "OrigReleaseDate",
                    "unique": False,
                    "label": "Orig Release Date",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "TitleNameWithFormat",
                    "unique": False,
                    "label": "Title Name With Format",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "TitleNameWithYear",
                    "unique": False,
                    "label": "Title Name With Year",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "int",
                    "name": "ProductionNumber",
                    "unique": False,
                    "label": "Production Number",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "int",
                    "name": "SeasonNumber",
                    "unique": False,
                    "label": "Season Number",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "Description",
                    "unique": False,
                    "label": "Description",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "LocalTitles",
                    "unique": False,
                    "label": "Local Titles",
                    "filterable": False,
                    "createable": True,
                    "updateable": False,
                    "nillable": True,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "datetime",
                    "name": "LastUpdateDate",
                    "unique": True,
                    "label": "Last Updated Date",
                    "filterable": True,
                    "idLookup": "LastUpdateDate",
                    "createable": True,
                    "updateable": False,
                    "nillable": False,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "list",
                    "name": "TitleSources",
                    "unique": False,
                    "label": "Title Sources",
                    "filterable": True,
                    "createable": True,
                    "updateable": False,
                    "nillable": False,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "list",
                    "name": "Characters",
                    "unique": False,
                    "label": "Characters",
                    "filterable": True,
                    "createable": True,
                    "updateable": False,
                    "nillable": False,
                    "defaultedOnCreate": False,
                },
                {
                    "type": "string",
                    "name": "TitleCredits",
                    "unique": False,
                    "label": "TitleCredits",
                    "filterable": True,
                    "createable": True,
                    "updateable": False,
                    "nillable": False,
                    "defaultedOnCreate": False,
                },
            ],
        }
        LOGGER.info(entity, entity_identifier)
        return CTAMResponse(status_code=200, response=json.dumps(entity), error_reason="")


# feilds = {
#             "fields": [
#                 {
#                 "type": "string",
#                 "name": "breed",
#                 "unique": True,
#                 "label": "breed",
#                 "filterable": True,
#                 "idLookup": "testIdLookup",
#                 "createable": True,
#                 "updateable": False,
#                 "nillable": False,
#                 "defaultedOnCreate": False
#                 },
#                 {
#                 "type": "struct",
#                 "name": "testField2",
#                 "unique": True,
#                 "label": "testLabel",
#                 "filterable": True,
#                 "externalId": "testId",
#                 "createable": True,
#                 "updateable": True,
#                 "nillable": False,
#                 "defaultedOnCreate": False
#                 }
#             ]
#             }

# {
#             "LastUpdateDate": "2016-06-05T07:24:04+00:00",
#             "LocalTitles": null,
#             "TitleSources": [
#                 {
#                     "SourceAltID": "20101854|27",
#                     "SourceAltIDType": "MARVEL Title ID",
#                     "LastUpdateDate": "2019-03-03T03:37:14+00:00",
#                     "StatusID": 1,
#                     "CreateDate": "2016-06-05T00:20:21+00:00",
#                     "CreatorID": "bisws006",
#                     "UpdatedByID": "bisws007"
#                 }
#             ],
#             "Characters": [
#
#             ],
#             "TitleCredits": null,
#             "ParentTitles": [
#
#             ],
#             "TitleID": 958,
#             "StatusID": 1,
#             "TitleTypeID": 7,
#             "TitleFormatID": 27,
#             "TitleAlternateIds": null,
#             "TitleTalents": null,
#             "TitleProductionCompany": null,
#             "EpisodeNumber": null,
#             "ForeignEpisodeNumber": null,
#             "TitleRatings": null,
#             "CreateDate": "2016-06-05T03:14:50+00:00",
#             "CreatorID": "bisws006",
#             "UpdatedByID": "bisws006",
#             "OriginalTitleName": "Incredible Hulk #231 (1968) Prelude!",
#             "StandardizedTitleName": "Incredible Hulk #231 Prelude!",
#             "DisambiguatedTitleName": "Incredible Hulk (1968): #231 Prelude!",
#             "OrigReleaseDate": "1979-01-01T00:00:00+00:00",
#             "TitleNameWithFormat": null,
#             "TitleNameWithYear": null,
#             "ProductionNumber": null,
#             "SeasonNumber": null,
#             "Description": null
#         }
