-- define a cte for ta
with ta_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__trvl_agcy_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for tac
tac_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__trvl_agcy_comm_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

--define a cte for cmps
cmps_cte as (
    select * from {{ ref('sil__intermediate__dreams__accounting__cmps_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- join ta, tac and cmps ctes to get the final result
final as (
    select
        tac.data_trvl_agcy_comm_id as travel_agency_commission_id,
        ta.data_trvl_agcy_id as travel_agency_id,
        ta.data_trvl_agcy_ods_id as travel_agency_external_orginization_id,
        ta.data_iata_id as iata_id,
        ta.data_cmps_id as campus_id,
        cmps.data_cmps_nm as campus_name,
        ta.data_sap_vndr_id as sap_vendor_id,
        ta.data_trvl_agcy_nm as travel_agency_name,
        tac.data_comm_sts_nm as commission_status_name,
        tac.data_fac_id as facility_id,
        null as facility_name,
        tac.data_root_chrg_grp_id as root_charge_group_id,
        tac.data_res_rspb_pty_id as reservation_responsible_party_id,
        tac.data_chrg_grp_chkin_dt as charge_group_checkin_date,
        tac.data_chrg_grp_chkot_dt as charge_group_checkout_date,
        tac.data_comm_apprvl_dt as commission_approval_date,
        tac.data_comm_ap_intfc_id as commission_ap_interface_id,
        tac.data_comm_pst_dts as commission_post_datetime,
        ta.data_trvl_agcy_pay_comm_in as travel_agency_pay_commission_indicator,
        ta.data_trvl_agcy_actv_in as travel_agency_active_indicator,
        ta.data_trvl_agcy_fm_create_dt as travel_agency_fm_create_dt,
        ta.data_glbl_tkt_comm_in as global_ticket_commission_indicator,
        tac.data_create_usr_id_cd as travel_agency_commission_create_user_id,
        tac.data_create_dts as travel_agency_commission_create_datetime,
        to_date(
            tac.data_create_dts
        ) as travel_agency_commission_create_date,
        ta.data_updt_usr_id_cd as travel_agency_user_id,
        ta.data_updt_dts as travel_agency_source_update_datetime,
        to_date(
            ta.data_updt_dts
        ) as travel_agency_source_update_date
    from ta_cte ta
    inner join tac_cte tac on ta.data_trvl_agcy_id = tac.data_trvl_agcy_id
    and ta.data_cmps_id = tac.data_cmps_id
    inner join cmps_cte cmps on tac.data_cmps_id = cmps.data_cmps_id
)

-- select from the final result cte
select * from final