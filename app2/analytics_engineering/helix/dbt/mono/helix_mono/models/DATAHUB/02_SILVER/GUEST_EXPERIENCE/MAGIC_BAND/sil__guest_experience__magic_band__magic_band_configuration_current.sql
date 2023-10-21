with cte_exprnc_band_config as (
    select *
    ---from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_config_versioned
	   from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_config_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_exprnc_band_dsny_prod as (
    select *
    --from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_dsny_prod_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_dsny_prod_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_exprnc_band_manu_tool as (
    select *
     -- from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_manu_tool_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_manu_tool_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_exprnc_band_mdle_config as (
    select *
    --from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_mdle_config_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_config_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_exprnc_band_mdle as (
    select *
    --from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_mdle_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_exprnc_band_mdle_vrsn as (
    select *
    --from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_mdle_vrsn_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_mdle_vrsn_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_exprnc_band_vndr as (
    select *
    --from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_vndr_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_vndr_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_top_color as (
    select *
    --from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_color_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_bottom_color as (
    select *
    --from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_color_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_color_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),


cte_exprnc_band_typ as (
    select *
    --from latest_datahub.sil_intermediate_xbms_wdw.exprnc_band_typ_versioned
	from  {{ ref('sil__intermediate__xbms__wdw__exprnc_band_typ_versioned') }}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
),

final_query as (
	
select distinct 
    exprnc_band_config.data_exprnc_band_config_id as configuration_id,
    exprnc_band_config.data_exprnc_band_dsny_prod_id as product_id,
    exprnc_band_dsny_prod.data_exprnc_band_typ_id as magic_band_type_id,
    exprnc_band_typ.data_exprnc_band_typ_cd as type_code,
    exprnc_band_typ.data_exprnc_band_typ_ds as type_description,
    exprnc_band_dsny_prod.data_exprnc_band_top_color_id as top_color_id,
    top_color.data_exprnc_band_color_cd as top_color_code,
    top_color.data_exprnc_band_color_nm as top_color_name,
    exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id as bottom_color_id,
    bottom_color.data_exprnc_band_color_cd as bottom_color_code,
    bottom_color.data_exprnc_band_color_nm as bottom_color_name,
    exprnc_band_config.data_exprnc_band_manu_tool_id as manufacture_tool_id,
    exprnc_band_manu_tool.data_exprnc_band_manu_tool_cd as manufacture_tool_code,
    exprnc_band_manu_tool.data_exprnc_band_manu_tool_ds as manufacture_tool_description,
    exprnc_band_config.data_exprnc_band_mdle_config_id as module_configuration_id,
    exprnc_band_mdle_config.data_exprnc_band_mdle_id as module_id,
    exprnc_band_mdle.data_exprnc_band_mdle_cd as module_code,
    exprnc_band_mdle.data_exprnc_band_mdle_ds as module_description,
    exprnc_band_mdle_config.data_exprnc_band_mdle_vrsn_id as module_version_id,
    exprnc_band_mdle_vrsn.data_exprnc_band_mdle_vrsn_cd as module_version_code,
    exprnc_band_mdle_vrsn.data_exprnc_band_mdle_vrsn_ds as module_version_description,
    exprnc_band_config.data_exprnc_band_vndr_id as vendor_id,
    exprnc_band_vndr.data_exprnc_band_vndr_cd as vendor_code,
    exprnc_band_vndr.data_exprnc_band_vndr_nm as vendor_name,
    exprnc_band_vndr.data_sap_id as sap_id,
    exprnc_band_config.data_exprnc_band_config_ds as configuration_description,
    exprnc_band_config.data_avail_to_gst_in as available_to_guest_indicator,
    exprnc_band_config.data_exprnc_band_config_cnfirm_in as configuration_confirmed_indicator,
    exprnc_band_config.data_create_usr_id as source_system_create_user_id,
    exprnc_band_config.data_create_dts as source_system_create_datetime,
    exprnc_band_config.data_updt_usr_id as source_system_update_user_id,
    exprnc_band_config.data_updt_dts as source_system_update_datetime,
    exprnc_band_config.data_logical_del_in as source_system_logical_delete_indicator
from 

cte_exprnc_band_config exprnc_band_config 
join cte_exprnc_band_dsny_prod exprnc_band_dsny_prod
on exprnc_band_dsny_prod.data_exprnc_band_dsny_prod_id = exprnc_band_config.data_exprnc_band_dsny_prod_id 

join cte_exprnc_band_manu_tool exprnc_band_manu_tool
on exprnc_band_manu_tool.data_exprnc_band_manu_tool_id = exprnc_band_config.data_exprnc_band_manu_tool_id 

join cte_exprnc_band_mdle_config exprnc_band_mdle_config
on exprnc_band_mdle_config.data_exprnc_band_mdle_config_id = exprnc_band_config.data_exprnc_band_config_id 

join cte_exprnc_band_mdle exprnc_band_mdle
on exprnc_band_mdle.data_exprnc_band_mdle_id = exprnc_band_mdle_config.data_exprnc_band_mdle_id 

join cte_exprnc_band_mdle_vrsn exprnc_band_mdle_vrsn
on exprnc_band_mdle_vrsn.data_exprnc_band_mdle_vrsn_id = exprnc_band_mdle_config.data_exprnc_band_mdle_vrsn_id 

join cte_exprnc_band_vndr exprnc_band_vndr
on exprnc_band_vndr.data_exprnc_band_vndr_id = exprnc_band_config.data_exprnc_band_vndr_id 

join cte_top_color top_color
on top_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_top_color_id 

join cte_bottom_color bottom_color
on bottom_color.data_exprnc_band_color_id = exprnc_band_dsny_prod.data_exprnc_band_bottom_color_id 

join cte_exprnc_band_typ exprnc_band_typ
on exprnc_band_typ.data_exprnc_band_typ_id = exprnc_band_dsny_prod.data_exprnc_band_typ_id
   )

select * from final_query