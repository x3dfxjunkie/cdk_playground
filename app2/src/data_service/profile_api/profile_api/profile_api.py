import json
import logging
import os
import re

import boto3
import pandas as pd
import snowflake.connector
from aws_lambda_powertools import Logger
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

logger = Logger(service=__name__)

ssm_client = boto3.client("ssm")


def lambda_handler(event: dict, _context):

    ssm_config_path = (
        event.get("ssm_config_path")
        if event.get("ssm_config_path")
        else os.environ.get("ssm_config_path")
    )

    ssm_config = ssm_client.get_parameter(Name=ssm_config_path, WithDecryption=True)
    if ssm_config is not None:
        logger.info("was able to get ssm creds for path %s", ssm_config_path)

    data = {
        "swid": "{0899a47f-b4c3-7712-f731-31eb22a6f139}",
        "abdFutureStayIndicator": True,
        "aulFutureStayIndicator": True,
        "bchFutureStayIndicator": True,
        "dclFutureStayIndicator": True,
        "dlrOnsiteFutureStayIndicator": True,
        "dlrGoodNeighborHotelFutureStayIndicator": True,
        "wdwOnsiteFutureStayIndicator": True,
        "wdwFutureGroupBookingSuppressionIndicator": True,
        "abdMinimumFutureArrivalDate": "2022-09-10",
        "aulMinimumFutureArrivalDate": "2022-09-10",
        "bchMinimumFutureArrivalDate": "2022-09-10",
        "dclMinimumFutureArrivalDate": "2022-09-10",
        "dlrOnsiteMinimumFutureArrivalDate": "2022-09-10",
        "dlrGoodNeighborHotelMinimumFutureArrivalDate": "2022-09-10",
        "wdwOnsiteMinimumFutureArrivalDate": "2022-09-10",
        "dlrOnsiteFutureArrival6MonthIndicator": True,
        "dlrGoodNeighborHotelFutureArrival6MonthIndicator": True,
        "wdwOnsiteFutureArrival6MonthIndicator": True,
        "abdMaximumPastStayDate": "2022-09-10",
        "aulMaximumPastStayDate": "2022-09-10",
        "bchMaximumPastStayDate": "2022-09-10",
        "dclMaximumPastStayDate": "2022-09-10",
        "dlrMaximumPastStayDate": "2022-09-10",
        "wdwMaximumPastStayDate": "2022-09-10",
        "abdMaximumLeadInteractionDate": "2022-09-10",
        "aulMaximumLeadInteractionDate": "2022-09-10",
        "dclMaximumLeadInteractionDate": "2022-09-10",
        "dlrMaximumLeadInteractionDate": "2022-09-10",
        "wdwMaximumLeadInteractionDate": "string",
        "dlrMaximumParkVisitDate": "2022-09-10",
        "wdwMaximumParkVisitDate": "2022-09-10",
        "dlrLegacyAnnualPassholderIndicator": True,
        "dlrLapsedAnnualPassIndicator": True,
        "wdwLapsedAnnualPassIndicator": True,
        "dlrLapsedAnnualPassholderPreviousExpirationDate": "2022-09-10",
        "wdwLapsedAnnualPassholderPreviousExpirationDate": "2022-09-10",
        "dlrActiveAnnualPassholderIndicator": True,
        "wdwActiveAnnualPassholderIndicator": True,
        "dlrActiveAnnualPassTypeName": "2022-09-10",
        "wdwActiveAnnualPassTypeName": "2022-09-10",
        "dvcMemberIndicator": True,
        "dvcTypeName": "2022-09-10",
        "dclFutureBlackPearlIndicator": True,
        "dclHomePortCode": "string",
        "castMemberIndicator": True,
        "castMemberAddressIndicator": True,
        "hispanicAudienceIndicator": True,
        "satoIndicator": True,
        "maximumFranchiseAffinity": "2022-09-10",
        "caslFooterIndicator": True,
        "householdLifestage": "string",
        "childIndicator": True,
        "ageOfYoungestChild": 18,
        "ageOfOldestChild": 18,
        "childAge0To5Indicator": True,
        "childAge6To9Indicator": True,
        "childAge8To15Indicator": True,
        "childAge10To13Indicator": True,
        "childAge14To17Indicator": True,
        "firstNameHygieneIndicator": True,
        "lastNameHygieneIndicator": True,
        "distanceToDlr": 0,
        "distanceToWdw": 0,
        "westOfRockiesStateIndicator": True,
        "eastOfRockiesStateIndicator": True,
        "northernCaliforniaIndicator": True,
        "southernCaliforniaIndicator": True,
        "floridaResidentIndicator": True,
        "hawaiiIndicator": True,
        "puertoRicoIndicator": True,
        "usaTerritoryIndicator": True,
        "usMilitaryBaseIndicator": True,
        "canadaEastIndicator": True,
        "canadaWestIndicator": True,
        "canadianQuebecProvinceIndicator": True,
        "designatedMarketingAreaCode": "string",
        "designatedMarketingAreaDescription": "string",
        "hotmailOrGmailDomainEmailWithA6MonthEngagementIndicator": True,
        "emailSharedIndicator": True,
        "email24MonthPositiveInteractionIndicator": True,
        "emailMaximumPositiveInteractionDate": "string",
        "emailMaximumEngagementDate": "2022-09-10",
        "dlrParkReservationFutureBookedIndicator": True,
        "wdwParkReservationFutureBookedIndicator": True,
        "dlrParkReservationMinimumFutureStartDate": "2022-09-10",
        "wdwParkReservationMinimumFutureStartDate": "2022-09-10",
        "dlrActiveDpiEntitlement": True,
        "wdwActiveDpiEntitlement": True,
        "disneyAffinityScoreDisneyBrand": 4,
        "disneyAffinityScoreFrozenFranchise": 4,
        "disneyAffinityScoreMarvelBrand": 4,
        "disneyAffinityScoreMickeyAndFriendsFranchise": 4,
        "disneyAffinityScoreNationalGeographicBrand": 4,
        "disneyAffinityScorePixarBrand": 4,
        "disneyAffinityScoreDisneyPrincessFranchise": 4,
        "disneyAffinityScoreStarWarsBrand": 4,
        "brazeDeltaChangeDateTimestamp": "2022-09-10T01:32:09.298Z",
        "etlLoadTimestamp": "2022-09-10T01:32:09.298Z",
    }
    return {"statusCode": "200", "body": json.dumps(data)}


# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# ssm_client = boto3.client(
#     "ssm", endpoint_url="http://host.docker.internal:4566")


# def get_connection(
#     user: str,
#     account: str,
#     warehouse: str,
#     database: str,
#     schema: str,
#     key: str,
#     key_passphrase: str,
# ) -> snowflake.connector.SnowflakeConnection:

#     connection = None

#     p_key = serialization.load_pem_private_key(
#         key.encode("raw_unicode_escape"),
#         password=key_passphrase.encode(),
#         backend=default_backend(),
#     )

#     pkb = p_key.private_bytes(
#         encoding=serialization.Encoding.DER,
#         format=serialization.PrivateFormat.PKCS8,
#         encryption_algorithm=serialization.NoEncryption(),
#     )

#     connection = snowflake.connector.connect(
#         user=user,
#         account=account,
#         private_key=pkb,
#         warehouse=warehouse,
#         database=database,
#         schema=schema,
#     )

#     return connection


# def lambda_handler(event: dict, _context):
#     db_config = ssm_client.get_parameter(
#         Name="/data-services/profile-api/profile-api-db-config")
#     db_account = db_config.get("account")
#     db_user = db_config.get("user")
#     db_warehouse = db_config.get("warehouse")
#     db_database = db_config.get("database")
#     db_schema = db_config.get("schema")

#     db_key = db_config.get("private_key")
#     db_key_passphrase = db_config.get("private_key_passphrase")

#     swid = event.get("swid")
#     if not swid or not re.match("^{[a-z|A-Z|\d|-]+}$", swid):
#         return {}  # TODO - also add http response code / 400?

#     connection = None
#     try:
#         connection = get_connection(
#             user=db_user,
#             account=db_account,
#             database=db_database,
#             schema=db_schema,
#             warehouse=db_warehouse,
#             key=db_key,
#             key_passphrase=db_key_passphrase,
#         )

#         sql = f"""SELECT SWID AS "swid",
#                     TRY_TO_BOOLEAN(ABD_FUT_STY_IN) AS "abdFutureStayIndicator",
#                     TRY_TO_BOOLEAN(AUL_FUT_STY_IN) AS "aulFutureStayIndicator",
#                     TRY_TO_BOOLEAN(BCH_FUT_STY_IN) AS "bchFutureStayIndicator",
#                     TRY_TO_BOOLEAN(DCL_FUT_STY_IN) AS "dclFutureStayIndicator",
#                     TRY_TO_BOOLEAN(DLR_ONST_FUT_STY_IN) AS "dlrOnsiteFutureStayIndicator",
#                     TRY_TO_BOOLEAN(DLR_GNH_FUT_STY_IN) AS "dlrGoodNeighborHotelFutureStayIndicator",
#                     TRY_TO_BOOLEAN(WDW_ONST_FUT_STY_IN) AS "wdwOnsiteFutureStayIndicator",
#                     TRY_TO_BOOLEAN(WDW_FUT_GRP_BKNG_SUPP_IN) AS "wdwFutureGroupBookingSuppressionIndicator",
#                     ABD_MIN_FUT_ARVL_DT AS "abdMinimumFutureArrivalDate",
#                     AUL_MIN_FUT_ARVL_DT AS "aulMinimumFutureArrivalDate",
#                     BCH_MIN_FUT_ARVL_DT AS "bchMinimumFutureArrivalDate",
#                     DCL_MIN_FUT_ARVL_DT AS "dclMinimumFutureArrivalDate",
#                     DLR_ONST_MIN_FUT_ARVL_DT AS "dlrOnsiteMinimumFutureArrivalDate",
#                     DLR_GNH_MIN_FUT_ARVL_DT AS "dlrGoodNeighborHotelMinimumFutureArrivalDate",
#                     WDW_ONST_MIN_FUT_ARVL_DT AS "wdwOnsiteMinimumFutureArrivalDate",
#                     TRY_TO_BOOLEAN(DLR_ONST_FUT_ARVL_6_MTH_IN) AS "dlrOnsiteFutureArrival6MonthIndicator",
#                     TRY_TO_BOOLEAN(DLR_GNH_FUT_ARVL_6_MTH_IN) AS "dlrGoodNeighborHotelFutureArrival6MonthIndicator",
#                     TRY_TO_BOOLEAN(WDW_ONST_FUT_ARVL_6_MTH_IN) AS "wdwOnsiteFutureArrival6MonthIndicator",
#                     ABD_MAX_PST_STY_DT AS "abdMaximumPastStayDate",
#                     AUL_MAX_PST_STY_DT AS "aulMaximumPastStayDate",
#                     BCH_MAX_PST_STY_DT AS "bchMaximumPastStayDate",
#                     DCL_MAX_PST_STY_DT AS "dclMaximumPastStayDate",
#                     DLR_MAX_PST_STY_DT AS "dlrMaximumPastStayDate",
#                     WDW_MAX_PST_STY_DT AS "wdwMaximumPastStayDate",
#                     ABD_MAX_LEAD_INTRCT_DT AS "abdMaximumLeadInteractionDate",
#                     AUL_MAX_LEAD_INTRCT_DT AS "aulMaximumLeadInteractionDate",
#                     DCL_MAX_LEAD_INTRCT_DT AS "dclMaximumLeadInteractionDate",
#                     DLR_MAX_LEAD_INTRCT_DT AS "dlrMaximumLeadInteractionDate",
#                     WDW_MAX_LEAD_INTRCT_DT AS "wdwMaximumLeadInteractionDate",
#                     DLR_MAX_PARK_VST_DT AS "dlrMaximumParkVisitDate",
#                     WDW_MAX_PARK_VST_DT AS "wdwMaximumParkVisitDate",
#                     TRY_TO_BOOLEAN(DLR_LGCY_AP_IN) AS "dlrLegacyAnnualPassholderIndicator",
#                     TRY_TO_BOOLEAN(DLR_LPSD_AP_IN) AS "dlrLapsedAnnualPassIndicator",
#                     TRY_TO_BOOLEAN(WDW_LPSD_AP_IN) AS "wdwLapsedAnnualPassIndicator",
#                     DLR_LPSD_AP_PREV_EXP_DT AS "dlrLapsedAnnualPassholderPreviousExpirationDate",
#                     WDW_LPSD_AP_PREV_EXP_DT AS "wdwLapsedAnnualPassholderPreviousExpirationDate",
#                     TRY_TO_BOOLEAN(DLR_ACTV_AP_IN) AS "dlrActiveAnnualPassholderIndicator",
#                     TRY_TO_BOOLEAN(WDW_ACTV_AP_IN) AS "wdwActiveAnnualPassholderIndicator",
#                     DLR_ACTV_AP_TYP_NM AS "dlrActiveAnnualPassTypeName",
#                     WDW_ACTV_AP_TYP_NM AS "wdwActiveAnnualPassTypeName",
#                     TRY_TO_BOOLEAN(DVC_MBR_IN) AS "dvcMemberIndicator",
#                     DVC_TYPE_NM AS "dvcTypeName",
#                     TRY_TO_BOOLEAN(DCL_FUT_BLK_PRL_IN) AS "dclFutureBlackPearlIndicator",
#                     DCL_HM_PRT_CD AS "dclHomePortCode",
#                     TRY_TO_BOOLEAN(CAST_MBR_IN) AS "castMemberIndicator",
#                     TRY_TO_BOOLEAN(CAST_MBR_ADDR_IN) AS "castMemberAddressIndicator",
#                     TRY_TO_BOOLEAN(HSP_AUD_IN) AS "hispanicAudienceIndicator",
#                     TRY_TO_BOOLEAN(SATO_IN) AS "satoIndicator",
#                     MAX_FRNCHS_AFFNTY AS "maximumFranchiseAffinity",
#                     TRY_TO_BOOLEAN(CASL_FOOT_IN) AS "caslFooterIndicator",
#                     HSHOLD_LIFESTAGE AS "householdLifestage",
#                     TRY_TO_BOOLEAN(CHLD_IN) AS "childIndicator",
#                     AGE_YNGST_CHLD AS "ageOfYoungestChild",
#                     AGE_OLDST_CHLD AS "ageOfOldestChild",
#                     TRY_TO_BOOLEAN(CHLD_0_5_IN) AS "childAge0To5Indicator",
#                     TRY_TO_BOOLEAN(CHLD_6_9_IN) AS "childAge6To9Indicator",
#                     TRY_TO_BOOLEAN(CHLD_8_15_IN) AS "childAge8To15Indicator",
#                     TRY_TO_BOOLEAN(CHLD_10_13_IN) AS "childAge10To13Indicator",
#                     TRY_TO_BOOLEAN(CHLD_14_17_IN) AS "childAge14To17Indicator",
#                     TRY_TO_BOOLEAN(FRST_NM_HYG_IN) AS "firstNameHygieneIndicator",
#                     TRY_TO_BOOLEAN(LST_NM_HYG_IN) AS "lastNameHygieneIndicator",
#                     DIST_2_RSRT_DLR AS "distanceToDlr",
#                     DIST_2_RSRT_WDW AS "distanceToWdw",
#                     TRY_TO_BOOLEAN(WOR_IN) AS "westOfRockiesStateIndicator",
#                     TRY_TO_BOOLEAN(EOR_IN) AS "eastOfRockiesStateIndicator",
#                     TRY_TO_BOOLEAN(NOCAL_IN) AS "northernCaliforniaIndicator",
#                     TRY_TO_BOOLEAN(SOCAL_IN) AS "southernCaliforniaIndicator",
#                     TRY_TO_BOOLEAN(FLRES_IN) AS "floridaResidentIndicator",
#                     TRY_TO_BOOLEAN(HI_IN) AS "hawaiiIndicator",
#                     TRY_TO_BOOLEAN(PR_IN) AS "puertoRicoIndicator",
#                     TRY_TO_BOOLEAN(US_TERR_IN) AS "usaTerritoryIndicator",
#                     TRY_TO_BOOLEAN(US_MLTRY_IN) AS "usMilitaryBaseIndicator",
#                     TRY_TO_BOOLEAN(CAN_EAST_IN) AS "canadaEastIndicator",
#                     TRY_TO_BOOLEAN(CAN_WEST_IN) AS "canadaWestIndicator",
#                     TRY_TO_BOOLEAN(CAN_QC_IN) AS "canadianQuebecProvinceIndicator",
#                     DMA_CD AS "designatedMarketingAreaCode",
#                     DMA_DESC AS "designatedMarketingAreaDescription",
#                     TRY_TO_BOOLEAN(EML_HM_GM_6MNTH_ENGMNT_IN) AS "hotmailOrGmailDomainEmailWithA6MonthEngagementIndicator",
#                     TRY_TO_BOOLEAN(EML_SHRD_IN) AS "emailSharedIndicator",
#                     TRY_TO_BOOLEAN(EML_24_POS_INTRCT_IN) AS "email24MonthPositiveInteractionIndicator",
#                     EML_MAX_POS_INTRCT_DT AS "emailMaximumPositiveInteractionDate",
#                     EML_MAX_ENGMNT_DT AS "emailMaximumEngagementDate",
#                     TRY_TO_BOOLEAN(DLR_PARK_RES_FUT_BKD_IN) AS "dlrParkReservationFutureBookedIndicator",
#                     TRY_TO_BOOLEAN(WDW_PARK_RES_FUT_BKD_IN) AS "wdwParkReservationFutureBookedIndicator",
#                     DLR_PARK_RES_FUT_STRT_DT AS "dlrParkReservationMinimumFutureStartDate",
#                     WDW_PARK_RES_FUT_STRT_DT AS "wdwParkReservationMinimumFutureStartDate",
#                     TRY_TO_BOOLEAN(DLR_ACTV_DPI_ENTTL) AS "dlrActiveDpiEntitlement",
#                     TRY_TO_BOOLEAN(WDW_ACTV_DPI_ENTTL) AS "wdwActiveDpiEntitlement",
#                     DPLUS_AFF_574848 AS "disneyAffinityScoreDisneyBrand",
#                     DPLUS_AFF_827762 AS "disneyAffinityScoreFrozenFranchise",
#                     DPLUS_AFF_051107 AS "disneyAffinityScoreMarvelBrand",
#                     DPLUS_AFF_223015 AS "disneyAffinityScoreMickeyAndFriendsFranchise",
#                     DPLUS_AFF_100107 AS "disneyAffinityScoreNationalGeographicBrand",
#                     DPLUS_AFF_122703 AS "disneyAffinityScorePixarBrand",
#                     DPLUS_AFF_127127 AS "disneyAffinityScoreDisneyPrincessFranchise",
#                     DPLUS_AFF_091902 AS "disneyAffinityScoreStarWarsBrand",
#                     BRAZE_DLTA_CHG_DTS AS "brazeDeltaChangeDateTimestamp",
#                     LOAD_DTS AS "etlLoadTimestamp"
#                 FROM PD_CCP_BASE_DB.WDPR_DRVR_ATTRIB_SMRY_SWID t
#                 WHERE t.swid = %(swid)s"""

#         df = pd.read_sql_query(sql=sql, con=connection, params={"swid": swid})
#         json_str = df.to_json(orient="records", date_format="iso")
#         json_value = json.loads(json_str)
#         return json_value

#     except Exception as error:
#         raise error
#     finally:
#         if connection:
#             connection.close()


# if __name__ == "__main__":
#     print(lambda_handler({}, None))
