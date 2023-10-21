WITH rsrc_own_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_own_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),
rsrc_own_ref_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_own_ref_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(metadata_operation) != 'DELETE'
),

final AS (
    SELECT
        ro.data_rsrc_own_id AS resource_owner_id,
        ro.data_asgn_ownr_id AS assigned_owner_id,
        ro.data_own_ds AS owner_description,
        ro.data_own_frm_dts AS owner_from_datetime,
        ro.data_own_end_dts AS owner_end_datetime,
        ror.data_extnl_own_ref_val AS external_owner_reference_value,
        ror.data_own_ref_typ_nm AS owner_reference_type_name,
        ro.data_orig_shr_ocpnt_in AS original_share_occupant_indicator,
        ro.data_onln_chkin_in AS online_checkin_indicator,
        ro.data_updt_dts AS source_update_datetime
    FROM
        rsrc_own_cte ro
        INNER JOIN rsrc_own_ref_cte ror
        ON ro.data_rsrc_own_id = ror.data_rsrc_own_id
    ORDER BY 1,2
)

SELECT * FROM final