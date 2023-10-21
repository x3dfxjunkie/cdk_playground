with tc_grp_cte as (
    select
        *
    from
       {{ ref('sil__intermediate__dreams__rooms_reservations__tc_grp_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
tps_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__tps_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
comnctn_chan_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__comnctn_chan_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
sls_chan_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__sls_chan_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
grp_tc_grp_chan_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__grp_tc_grp_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
grp_tm_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__grp_tm_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
tp_gthr_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__tp_gthr_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
tps_extnl_ref_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__rooms_reservations__tps_extnl_ref_versioned') }}
    where
        metadata_version_end_datetime = '9999-12-31 00:00:00.000000'
),
final as (
    select
        distinct tps.data_tp_id travel_plan_id,
        tg.data_tps_id travel_plan_segment_id,
        tg.data_tc_grp_nb as travel_component_group_number,
        tg.data_add_on_tc_grp_nb add_on_travel_component_group_number,
        tps.data_trvl_sts_nm travel_status_name,
        tps.data_tps_arvl_dt travel_plan_segment_arrival_date,
        tps.data_tps_dprt_dt travel_plan_segment_departure_date,
        tps.data_tps_est_arvl_tm travel_plan_segment_estimated_arrival_time,
        tps.data_tps_est_dprt_tm travel_plan_segment_estimated_departure_time,
        tps.data_vip_lvl_nm vip_level_name,
        tw.data_gthr_cd gather_code,
        tps.data_trvl_agcy_pty_id travel_agency_party_id,
        tps.data_trvl_agt_pty_id travel_agent_party_id,
        tps.data_tps_secur_vl travel_plan_segment_secure_value,
        tps.data_tps_ctct_nm travel_plan_segment_contact_name,
        tps.data_tps_cncl_dts travel_plan_segment_cancel_dts,
        tps.data_tps_cncl_nb travel_plan_segment_cancel_number,
        tps.data_tps_guar_in travel_plan_segment_guaranteed_indicator,
        tps.data_onst_phn_nb onsite_phone_number,
        tps.data_web_txfr_cd website_transfer_code,
        tps.data_trms_cndtns_vers_nb terms_conditions_version_number,
        tps.data_syw_opt_in service_your_way_option_in,
        tg.data_comnctn_chan_id communication_channel_id,
        cc.data_comnctn_chan_nm communication_channel_name,
        tg.data_sls_chan_id sales_channel_id,
        sc.data_sls_chan_nm sales_channel_name,
        tg.data_tc_grp_typ_nm travel_component_group_type_name,
        tg.data_adv_internt_chkin_in advance_internet_check_in_indicator,
        gtg.data_grp_cd group_code,
        gt.data_grp_tm_nm group_team_name,
        ter.data_tps_extnl_ref_typ_nm as travel_plan_segment_external_reference_type_name,
        ter.data_tps_src_nm as travel_plan_segment_external_reference_source_name,
        ter.data_tps_extnl_ref_vl as travel_plan_segment_external_reference_value,
        tps.data_create_dts as travel_plan_segment_data_create_dts,
        tps.data_create_usr_id_cd as travel_plan_segment_create_user_id_cd,
        tps.data_updt_dts as travel_plan_segment_source_update_dts,
        --- data_src_updt_dts is missing
        tps.data_updt_usr_id_cd as travel_plan_segment_update_user_id_code
    from
        tc_grp_cte tg
        inner join tps_cte tps
        on tg.data_tps_id = tps.data_tps_id
        left join comnctn_chan_cte cc
        on tg.data_comnctn_chan_id = cc.data_comnctn_chan_id
        left join sls_chan_cte sc
        on tg.data_sls_chan_id = sc.data_sls_chan_id
        left join grp_tc_grp_chan_cte gtg
        on tg.data_tc_grp_nb = gtg.data_tc_grp_nb
        left join grp_tm_cte gt
        on gtg.data_grp_tm_id = gt.data_grp_tm_id
        left join tp_gthr_cte tw
        on tps.data_tp_id = tw.data_tp_id
        left join tps_extnl_ref_cte ter
        on tps.data_tps_id = ter.data_tps_id
)
select
    *
from
    final
