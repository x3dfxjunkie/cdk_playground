-- Define a CTE for B
WITH b_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__folio__bill_versioned')}}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),

-- Define a CTE for BA
ba_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__folio__bill_aplcbl_versioned')}}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),

-- Join B and BA CTEs to get the final result
final AS (
    SELECT
        DISTINCT B.DATA_BILL_ID AS BILL_ID,
        B.DATA_BILL_CD_NM AS BILL_CODE_NAME,
        B.DATA_BILL_CD_DS AS BILL_CODE_DESCRIPTION,
        B.DATA_BILL_CD_STRT_DT AS BILL_CODE_START_DATE,
        B.DATA_BILL_CD_END_DT AS BILL_CODE_END_DATE,
        BA.DATA_REV_CLS_ID AS REVENUE_CLASS_ID,
        BA.DATA_BILL_APLCBL_STRT_DT AS BILL_APPLICABLE_START_DATE,
        BA.DATA_BILL_APLCBL_END_DT AS BILL_APPLICABLE_END_DATE,
        BA.DATA_PKG_ID AS PACKAGE_ID,
        BA.DATA_ADD_BY_PKGR_IN AS ADDED_BY_PACKAGER_INDICATOR
    FROM b_cte B
    INNER JOIN ba_cte BA ON B.DATA_BILL_ID = BA.DATA_BILL_ID
)

-- Select from the final result CTE
SELECT * FROM final