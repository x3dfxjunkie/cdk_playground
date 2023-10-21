with 
  cte_xb_exprnc_band_vndr as (
    select
     *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_xb_exp_band_vndr_stk_lvl as (
    select
      *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_stk_lvl_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_xb_vndr_invtry_item as (
    select
     *
    
	from {{ ref('sil__intermediate__xbms__wdw__vndr_invtry_item_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_xb_exprnc_band_vndr_invtry as (
    select
      *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_invtry_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_xb_exprnc_band_dsny_prod as (
    select
     *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_xb_exprnc_band_typ as (
    select
      *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_typ_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_xb_exprnc_band_mdle_config as (
    select
      *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_config_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_xb_exprnc_band_mdle as (
    select
     *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_top_color as (
    select
      *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
  ),
  cte_bottom_color as (
    select
      *
    
	from {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),
final_cte as (
    select
        xb_exprnc_band_vndr.data_exprnc_band_vndr_id as vendor_id,
        xb_exprnc_band_vndr.data_sap_id as vendor_sap_id,
        xb_exprnc_band_vndr.data_exprnc_band_vndr_nm as vendor_name,
        xb_exprnc_band_vndr.data_exprnc_band_vndr_cd as vendor_code,
        xb_exp_band_vndr_stk_lvl.data_exprnc_band_vndr_stk_lvl_id as vendor_stock_level_id,
        xb_exp_band_vndr_stk_lvl.data_vndr_band_actl_reord_pt_cn as actual_reorder_point_count,
        xb_exp_band_vndr_stk_lvl.data_vndr_band_rcmd_reord_pt_cn as recommended_reorder_point_count,
        xb_exp_band_vndr_stk_lvl.data_vndr_band_actl_sfty_stk_cn as actual_safety_stock_count,
        xb_exp_band_vndr_stk_lvl.data_vndr_band_rcmd_sfty_stk_cn as recommended_safety_stock_count,
        xb_exp_band_vndr_stk_lvl.data_vndr_band_actl_reord_qty_cn as actual_reorder_quantity_count,
        xb_exp_band_vndr_stk_lvl.data_vndr_band_rcmd_reord_qty_cn as recommended_reorder_quantity_count,
        xb_exp_band_vndr_stk_lvl.data_vndr_band_avail_for_po_in as available_for_purchase_order_indicator,
        xb_vndr_invtry_item.data_vndr_invtry_item_id as vendor_inventory_item_id,
        xb_vndr_invtry_item.data_exprnc_band_mdle_config_id as module_config_id,
        xb_exprnc_band_mdle.data_exprnc_band_mdle_cd as module_code,
        xb_exprnc_band_mdle.data_exprnc_band_mdle_ds as module_description,
        xb_vndr_invtry_item.data_exprnc_band_dsny_prod_id as product_id,
        xb_exprnc_band_dsny_prod.data_exprnc_band_typ_id as type_id,
        xb_exprnc_band_typ.data_exprnc_band_typ_cd as product_type_code,
        xb_exprnc_band_typ.data_exprnc_band_typ_ds as product_type_description,
        top_color.data_exprnc_band_color_nm as top_color_name,
        bottom_color.data_exprnc_band_color_nm as bottom_color_name,
        xb_exprnc_band_vndr_invtry.data_exprnc_band_vndr_invtry_id as vendor_inventory_id,
        xb_exprnc_band_vndr_invtry.data_invtry_on_hnd_cn as inventory_on_hand_count,
        xb_exprnc_band_vndr_invtry.data_invtry_comtd_cn as inventory_committed_count,
        xb_exprnc_band_vndr_invtry.data_invtry_avail_cn as inventory_available_count,
        xb_exprnc_band_vndr.data_logical_del_in as source_system_logical_delete_indicator,
        xb_exprnc_band_vndr.data_create_usr_id as source_system_create_user_id,
        xb_exprnc_band_vndr.data_create_dts as source_system_create_datetime,
        xb_exprnc_band_vndr.data_updt_usr_id as source_system_update_user_id,
        xb_exprnc_band_vndr.data_updt_dts as source_system_update_datetime
    from
cte_xb_exprnc_band_vndr xb_exprnc_band_vndr 
join cte_xb_exp_band_vndr_stk_lvl xb_exp_band_vndr_stk_lvl
on xb_exp_band_vndr_stk_lvl.data_exprnc_band_vndr_id = xb_exprnc_band_vndr.data_exprnc_band_vndr_id 
join cte_xb_vndr_invtry_item xb_vndr_invtry_item
on xb_vndr_invtry_item.data_vndr_invtry_item_id = xb_exp_band_vndr_stk_lvl.data_vndr_invtry_item_id 
left outer join cte_xb_exprnc_band_vndr_invtry xb_exprnc_band_vndr_invtry
on xb_exprnc_band_vndr_invtry.data_vndr_invtry_item_id = xb_vndr_invtry_item.data_vndr_invtry_item_id 
left outer join cte_xb_exprnc_band_dsny_prod xb_exprnc_band_dsny_prod
on xb_vndr_invtry_item.data_exprnc_band_dsny_prod_id = xb_exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id 
left outer join cte_xb_exprnc_band_typ xb_exprnc_band_typ
on xb_exprnc_band_dsny_prod.data_exprnc_band_typ_id = xb_exprnc_band_typ.data_exprnc_band_typ_id 
left outer join cte_xb_exprnc_band_mdle_config xb_exprnc_band_mdle_config
on xb_vndr_invtry_item.data_exprnc_band_mdle_config_id = xb_exprnc_band_mdle_config.data_exprnc_band_mdle_config_id 
left outer join cte_xb_exprnc_band_mdle xb_exprnc_band_mdle
on xb_exprnc_band_mdle_config.data_exprnc_band_mdle_id = xb_exprnc_band_mdle.data_exprnc_band_mdle_id 
left outer join cte_top_color top_color
on xb_exprnc_band_dsny_prod.data_exprnc_band_top_color_id = top_color.data_exprnc_band_color_id 
left outer join cte_bottom_color bottom_color
on xb_exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id = bottom_color.data_exprnc_band_color_id
)
select
    *
from
    final_cte
