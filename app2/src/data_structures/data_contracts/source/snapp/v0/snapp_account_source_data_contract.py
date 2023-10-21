"""Source Data Contract for SnApp Account"""

from __future__ import annotations
from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import GlobalSnAppHeader


class MetaDataListItem(BaseModel):
    """MetaDataListItem"""

    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="Meta Field Code",
        description="",
        example="FT1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="Meta Field Data Type",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_field_data_type_desc: str = Field(
        ...,
        alias="MetaFieldDataTypeDesc",
        name="Meta Field Data Type Desc",
        description="",
        example="Text",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="Meta Field Id",
        description="",
        example="52192699-6429-AB12-0044-0163D2B62603",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="Meta Field Name",
        description="",
        example="First Name",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_field_type: Optional[int] = Field(
        None,
        alias="MetaFieldType",
        name="Meta Field Type",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_field_type_desc: Optional[str] = Field(
        None,
        alias="MetaFieldTypeDesc",
        name="Meta Field Type Desc",
        description="",
        example="First Name",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="MARCIO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_field_item_name: Optional[str] = Field(
        None,
        alias="MetaFieldItemName",
        name="Meta Field Item Name",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Payload(BaseModel):
    """Payload"""

    ats_account_alias: Optional[str] = Field(
        None,
        alias="ATSAccountAlias",
        name="Ats Account Alias",
        description="",
        example="null",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    account_code: Optional[str] = Field(
        None,
        alias="AccountCode",
        name="Account Code",
        description="",
        example="PAWZA936881TCZPP4STR",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )
    account_code_ext: Optional[str] = Field(
        None,
        alias="AccountCodeExt",
        name="Account Code Ext",
        description="",
        example="PAWZA936881TCZPP4STR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    account_id: str = Field(
        ...,
        alias="AccountId",
        name="Account Id",
        description="",
        example="EE289949-CAB3-CB06-5299-01875BC61322",
        guest_identifier="true",
        transaction_identifier=False,
        identifier_tag="indirect",
    )
    account_status: Optional[int] = Field(
        None,
        alias="AccountStatus",
        name="Account Status",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    account_status_desc: Optional[str] = Field(
        None,
        alias="AccountStatusDesc",
        name="Account Status Desc",
        description="",
        example="Active",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_adjusted_hire_date: Optional[date] = Field(
        None,
        alias="CAGAdjustedHireDate",
        name="Cag Adjusted Hire Date",
        description="",
        example="2020-12-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_central_person_id: Optional[str] = Field(
        None,
        alias="CAGCentralPersonID",
        name="Cag Central Person Id",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_cost_center: Optional[str] = Field(
        None,
        alias="CAGCostCenter",
        name="Cag Cost Center",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_first_name: Optional[str] = Field(
        None,
        alias="CAGFirstName",
        name="Cag First Name",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    cag_last_name: Optional[str] = Field(
        None,
        alias="CAGLastName",
        name="Cag Last Name",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    cag_marital_status: Optional[str] = Field(
        None,
        alias="CAGMaritalStatus",
        name="Cag Marital Status",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_marital_status_desc: Optional[str] = Field(
        None,
        alias="CAGMaritalStatusDesc",
        name="Cag Marital Status Desc",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_middle_initial: Optional[str] = Field(
        None,
        alias="CAGMiddleInitial",
        name="Cag Middle Initial",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cagpernr: Optional[str] = Field(
        None,
        alias="CAGPERNR",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="indirect",
    )
    cag_personnel_area: Optional[str] = Field(
        None,
        alias="CAGPersonnelArea",
        name="Cag Personnel Area",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_site: Optional[str] = Field(
        None,
        alias="CAGSite",
        name="Cag Site",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_special_pass_code: Optional[str] = Field(
        None,
        alias="CAGSpecialPassCode",
        name="Cag Special Pass Code",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_special_pass_code_desc: Optional[str] = Field(
        None,
        alias="CAGSpecialPassCodeDesc",
        name="Cag Special Pass Code Desc",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    cag_spouse_first_name: Optional[str] = Field(
        None,
        alias="CAGSpouseFirstName",
        name="Cag Spouse First Name",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    cag_spouse_id: Optional[str] = Field(
        None,
        alias="CAGSpouseID",
        name="Cag Spouse Id",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cag_spouse_last_name: Optional[str] = Field(
        None,
        alias="CAGSpouseLastName",
        name="Cag Spouse Last Name",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    category_code: Optional[str] = Field(
        None,
        alias="CategoryCode",
        name="Category Code",
        description="",
        example="null",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    category_code_list: Optional[List[str]] = Field(
        None,
        alias="CategoryCodeList",
        name="Category Code List",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    category_id: Optional[str] = Field(
        None,
        alias="CategoryId",
        name="Category Id",
        description="",
        example="5C9CAF1A-2B1A-7C42-3ABA-016B8F5D55B0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    category_id_list: Optional[List[str]] = Field(
        None,
        alias="CategoryIdList",
        name="Category Id List",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    category_name_list: Optional[List[str]] = Field(
        None,
        alias="CategoryNameList",
        name="Category Name List",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    category_recursive_name: Optional[str] = Field(
        None,
        alias="CategoryRecursiveName",
        name="Category Recursive Name",
        description="",
        example="Guest Account",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    company_name1: Optional[str] = Field(
        None,
        alias="CompanyName1",
        name="Company Name 1",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    display_name: Optional[str] = Field(
        None,
        alias="DisplayName",
        name="Display Name",
        description="",
        example="Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    entity_type: Optional[int] = Field(
        None,
        alias="EntityType",
        name="Entity Type",
        description="",
        example=15,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entity_type_desc: Optional[str] = Field(
        None,
        alias="EntityTypeDesc",
        name="Entity Type Desc",
        description="",
        example="Person",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    first_name: Optional[str] = Field(
        None,
        alias="FirstName",
        name="First Name",
        description="",
        example="Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    lang_iso: Optional[str] = Field(
        None,
        alias="LangISO",
        name="Lang Iso",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="LastName",
        name="Last Name",
        description="",
        example="Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    license_id: Optional[int] = Field(
        None,
        alias="LicenseId",
        name="License Id",
        description="",
        example=1241,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    main_portfolio_id: Optional[str] = Field(
        None,
        alias="MainPortfolioId",
        name="Main Portfolio Id",
        description="",
        example="DBE0A747-4CC3-D484-5443-01875BC6168E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    middle_name: Optional[str] = Field(
        None,
        alias="MiddleName",
        name="Middle Name",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    parent_account_id: Optional[str] = Field(
        None,
        alias="ParentAccountId",
        name="Parent AccountId",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    profile_picture_id: Optional[str] = Field(
        None,
        alias="ProfilePictureId",
        name="Profile Picture Id",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_exempt_certificate_code: Optional[str] = Field(
        None,
        alias="TaxExemptCertificateCode",
        name="Tax Exempt Certificate Code",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_exempt_certificate_expiration: Optional[str] = Field(
        None,
        alias="TaxExemptCertificateExpiration",
        name="Tax Exempt Certificate Expiration",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    user_modification_action: Optional[str] = Field(
        None,
        alias="UserModificationAction",
        name="User Modification Action",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    user_modification_date: Optional[datetime] = Field(
        None,
        alias="UserModificationDate",
        name="User Modification Date",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    user_personnel_number: Optional[str] = Field(
        None,
        alias="UserPersonnelNumber",
        name="User Personnel Number",
        description="",
        example="null",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_data_list: Optional[List[MetaDataListItem]] = Field(
        None,
        alias="MetaDataList",
        name="Meta Data List",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SnAppAccountModel(BaseModel):
    """SnAppAccountModel"""

    class Config:
        """SnAppAccountModel Config"""

        title = "SnApp Account"
        stream_name = "prd-use1-guest360-snapp-stream"
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = ""
        key_path_name = "Header.Namespace"
        key_path_value = "SnApp.Account"

    header: GlobalSnAppHeader = Field(..., alias="Header", description="SnApp data metadata")
    payload: Payload = Field(
        ...,
        alias="Payload",
        description="Data payload",
    )
