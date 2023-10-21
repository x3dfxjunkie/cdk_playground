-- cte for HR
WITH hr_cte AS (
    SELECT
        DISTINCT rm.data_rsrc_id AS room_id,
        rit.data_rsrc_invtry_typ_id AS room_inventory_type_id,
        rit.data_rsrc_invtry_typ_cd AS room_type_code,
        rm.data_rm_id_vl AS room_number,
        rm.data_rsrt_fac_id AS facility_id,
        NULL AS facility_name,
        rm.data_rm_ds AS room_description
    FROM
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_invtry_typ_versioned') }}
        rit
        INNER JOIN {{ ref('sil__intermediate__dreams__resource_inventory_management__rm_versioned') }}
        rm
        ON rit.data_rsrc_invtry_typ_id = rm.data_rsrc_invtry_typ_id
        AND rit.metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(
            rit.metadata_operation
        ) != 'DELETE'
),
-- cte for CRL
crl_cte AS (
    SELECT
        *
    FROM
        {{ ref('sil__intermediate__dreams__resource_inventory_management__cnct_rm_lnk_versioned') }}
    WHERE
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(
            metadata_operation
        ) != 'DELETE'
),
-- cte for HR2
hr2_cte AS (
    SELECT
        DISTINCT rm.data_rsrc_id AS room_id,
        rit.data_rsrc_invtry_typ_id AS room_inventory_type_id,
        rit.data_rsrc_invtry_typ_cd AS room_type_code,
        rm.data_rsrt_fac_id AS rsrt_fac_id,
        rm.data_rm_id_vl AS rm_id_vl,
        rm.data_rm_nm AS rm_nm,
        rm.data_rm_ds AS rm_ds
    FROM
        {{ ref('sil__intermediate__dreams__resource_inventory_management__rsrc_invtry_typ_versioned') }}
        rit
        INNER JOIN {{ ref('sil__intermediate__dreams__resource_inventory_management__rm_versioned') }}
        rm
        ON rit.data_rsrc_invtry_typ_id = rm.data_rsrc_invtry_typ_id
        AND rm.metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        AND UPPER(
            rm.metadata_operation
        ) != 'DELETE'
),
FINAL AS (
    SELECT
        hr.*,
        hr2.room_id AS connected_resource_inventory_id,
        hr2.room_inventory_type_id AS connected_room_inventory_type_id,
        hr2.room_type_code AS connected_room_type_code,
        hr2.rm_id_vl AS connected_room_number,
        hr2.rm_ds AS connected_room_description
    FROM
        hr_cte hr
        LEFT JOIN crl_cte crl
        ON hr.room_id = crl.data_cnctg_rsrc_id
        LEFT JOIN hr2_cte hr2
        ON crl.data_cnctd_rsrc_id = hr2.room_id
)
SELECT
    *
FROM
    FINAL
