-- define a cte for xb_po
with xb_po_cte as (
    select
        *
    from {{ ref('sil__intermediate__xbms__wdw__po_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- define a cte for xb_po_item
xb_po_item_cte as (
    select
        *
    from {{ ref('sil__intermediate__xbms__wdw__po_item_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- define a cte for xb_po_sts
xb_po_sts_cte as (
    select
        *
    from {{ ref('sil__intermediate__xbms__wdw__po_sts_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- define a cte for xb_exprnc_band_vndr
xb_exprnc_band_vndr_cte as (
    select
        *
    from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- define a cte for xb_exprnc_band_vndr_rl
xb_exprnc_band_vndr_rl_cte as (
    select
        *
    from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_rl_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

-- join the ctes to get the final result
final as (
    select
        xb_po.data_po_id as magic_band_purchase_order_id,
        xb_po.data_exprnc_band_vndr_id as vendor_id,
        xb_exprnc_band_vndr.data_sap_id as vendor_sap_id,
        xb_exprnc_band_vndr.data_exprnc_band_vndr_nm as vendor_name,
        xb_exprnc_band_vndr.data_exprnc_band_vndr_cd as vendor_code,
        xb_exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_cd as vendor_role_code,
        xb_exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_ds as vendor_role_description,
        xb_po.data_exprnc_band_mfr_id as manufacturer_id,
        xb_po.data_po_nb as purchase_order_number,
        xb_po.data_po_placed_dt as placed_datetime,
        cast(xb_po.data_po_placed_dt as date) as placed_date,
        xb_po.data_po_expect_ship_dt as expected_shipment_datetime,
        cast(xb_po.data_po_expect_ship_dt as date) as expected_shipment_date,
        xb_po.data_po_expect_dlvr_dt as expected_delivery_datetime,
        cast(xb_po.data_po_expect_dlvr_dt as date) as expected_delivery_date,
        cast(xb_po.data_po_actl_ship_dt as date) as shipment_date,
        cast(xb_po.data_po_actl_dlvr_dt as date) as delivery_date,
        xb_po_item.data_po_item_id as purchase_order_item_id,
        xb_po_item.data_vndr_invtry_item_id as vendor_inventory_item_id,
        xb_po_item.data_po_item_cn as item_count,
        xb_po_sts.data_po_sts_id as purchase_order_status_id,
        xb_po_sts.data_po_sts_cd as status_code,
        xb_po_sts.data_po_sts_ds as status_description,
        xb_po.data_logical_del_in as source_system_logical_delete_indicator,
        xb_po.data_create_usr_id as source_system_create_user_id,
        xb_po.data_create_dts as source_system_create_datetime,
        xb_po.data_updt_usr_id as source_system_update_user_id,
        xb_po.data_updt_dts as source_system_update_datetime
    from xb_po_cte xb_po
    inner join xb_po_item_cte xb_po_item
    on xb_po.data_po_id = xb_po_item.data_po_id
    inner join xb_po_sts_cte xb_po_sts
    on xb_po.data_po_sts_id = xb_po_sts.data_po_sts_id
    inner join xb_exprnc_band_vndr_cte xb_exprnc_band_vndr
    on xb_po.data_exprnc_band_vndr_id = xb_exprnc_band_vndr.data_exprnc_band_vndr_id
    inner join xb_exprnc_band_vndr_rl_cte xb_exprnc_band_vndr_rl
    on xb_exprnc_band_vndr.data_exprnc_band_vndr_rl_id = xb_exprnc_band_vndr_rl.data_exprnc_band_vndr_rl_id
)

-- select from the final result cte
select * from final
