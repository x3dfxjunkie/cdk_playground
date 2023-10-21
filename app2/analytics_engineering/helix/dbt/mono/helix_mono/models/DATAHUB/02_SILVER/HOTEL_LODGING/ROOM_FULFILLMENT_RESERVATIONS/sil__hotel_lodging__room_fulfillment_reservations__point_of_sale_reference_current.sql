-- define a cte for cer
with cer_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_extnl_ref_versioned') }}
    where
        data_extnl_src_nm = 'app'
        and upper(metadata_operation) != 'DELETE'
        and metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
-- join ctes to get the final result
final as (
    select
        cer.data_chrg_id as charge_id,
        cer.data_chrg_extnl_ref_vl as reference_id,
        cer.data_create_usr_id_cd as create_user_id,
        cer.data_create_dts as create_datetime,
        to_date(
            cer.data_create_dts
        ) as create_date,
        cer.data_updt_usr_id_cd as update_user_id,
        cer.data_updt_dts as update_datetime,
        to_date(
            cer.data_updt_dts
        ) as update_date
    from
        cer_cte cer
)
select
    *
from
    final
