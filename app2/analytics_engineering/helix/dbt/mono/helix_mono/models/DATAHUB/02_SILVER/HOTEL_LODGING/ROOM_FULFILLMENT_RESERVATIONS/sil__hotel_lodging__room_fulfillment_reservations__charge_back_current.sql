with acb_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__acb_chrg_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
acbr_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__chrg_back_rsn_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cbc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__chrg_back_ctgy_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
final_cte as (
    select
        distinct acb.data_acb_chrg_id as auto_charge_back_charge_id,
        acb.data_chrg_back_ctgy_id as charge_back_category_id,
        cbc.data_chrg_back_ctgy_nm as charge_back_category_name,
        acb.data_chrg_back_rsn_id as charge_back_reason_id,
        acbr.data_chrg_back_rsn_nm as charge_back_reason_name,
        acb.data_chrg_back_loc_nm as charge_back_location_name,
        acb.data_create_dts as create_datetime,
        acb.data_create_usr_id_cd as create_user_id
    from
        acb_cte acb
        left join acbr_cte acbr
        on acb.data_chrg_back_rsn_id = acbr.data_chrg_back_rsn_id
        left join cbc_cte cbc
        on acb.data_chrg_back_ctgy_id = cbc.data_chrg_back_ctgy_id
)
select
    *
from
    final_cte
