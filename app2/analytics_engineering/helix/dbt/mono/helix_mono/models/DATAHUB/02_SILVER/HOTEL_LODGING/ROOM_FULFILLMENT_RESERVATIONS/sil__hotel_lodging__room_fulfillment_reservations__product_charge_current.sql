-- define a cte for pc
with pc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__prod_chrg_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for cmp
cmp_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_mkt_pkg_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for cmper
cmper_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__cmp_extnl_ref_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- join ctes to get the final result
final as(
    select
        distinct cmper.data_cmp_extnl_ref_vl as package_component_id,
        pc.data_chrg_id as product_charge_id,
        pc.data_prod_chrg_upgrd_typ_nm as product_charge_upgrade_type_name,
        pc.data_prod_id as product_id,
        pc.data_prod_cd as product_code,
        pc.data_prod_ds as product_description,
        pc.data_chrg_mkt_pkg_id as charge_market_package_id,
        cmp.data_pkg_id as package_id,
        cmp.data_pkg_ds as package_description,
        cmp.data_pkg_chan_id as package_channel_id,
        pc.data_prod_typ_nm as product_type_name,
        pc.data_comctn_chan_nm as communication_channel_name,
        pc.data_sls_chan_nm as sales_channel_name,
        pc.data_trvl_agt_id as travel_agent_id,
        pc.data_ovrd_prod_chrg_in as override_product_charge_indicator,
        pc.data_updt_dts as data_updt_dts
    from
        pc_cte pc
        inner join cmp_cte cmp
        on pc.data_chrg_mkt_pkg_id = cmp.data_chrg_mkt_pkg_id
        inner join cmper_cte cmper
        on cmp.data_chrg_mkt_pkg_id = cmper.data_chrg_mkt_pkg_id
)

select * from final
