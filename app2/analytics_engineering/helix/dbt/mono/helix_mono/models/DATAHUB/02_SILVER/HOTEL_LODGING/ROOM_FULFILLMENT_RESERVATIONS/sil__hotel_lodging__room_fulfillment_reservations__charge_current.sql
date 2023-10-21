-- define a cte for c
with c_cte as (
    select * from {{ ref('sil__intermediate__dreams__folio__chrg_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for tac
tac_cte as (
    select * from {{ ref('sil__intermediate__dreams__accounting__acct_ctr_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- define a cte for sac
sac_cte as (
    select * from {{ ref('sil__intermediate__dreams__accounting__acct_ctr_versioned')}}
    where metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
    and upper(metadata_operation) != 'DELETE'
),

-- join c, tac and tac ctes to get the final result
final as (
    select
        distinct c.data_chrg_id as charge_id,
        c.data_chrg_typ_nm as charge_type_name,
        c.data_chrg_ffl_dts as charge_fulfillment_datetime,
        to_date(data_chrg_ffl_dts) as charge_fulfillment_date,
        c.data_acct_dt as account_date,
        c.data_chrg_ds as charge_description,
        c.data_recog_sts_nm as recognition_status_name,
        c.data_chrg_grp_id as charge_group_id,
        c.data_chrg_by_nm as charge_by_name,
        c.data_txn_acct_ctr_id as transaction_account_center_id,
        tac.data_acct_ctr_nm as transaction_account_center_name,
        c.data_rev_cls_id as revenue_class_id,
        c.data_rev_cls_nm as revenue_class_name,
        c.data_chrg_am as charge_amount,
        c.data_chrg_actv_in as charge_active_indicator,
        c.data_src_acct_ctr_id as source_account_center_indicator,
        sac.data_acct_ctr_nm as source_account_center_name,
        c.data_sprsd_chrg_id as supressed_charge_id,
        c.data_chrg_rpst_in as charge_repost_indicator,
        c.data_exprnc_card_nb as experience_card_number,
        c.data_chrg_pst_st_nm as charge_post_status_name,
        c.data_folio_txn_typ_cd as folio_transaction_type_code,
        c.data_txn_idvl_pty_id as transaction_individual_party_id,
        c.data_chrg_pty_cn as charge_party_count,
        c.data_dvc_pts_vl as disney_vacation_club_points_value,
        c.data_wrk_loc_id as work_location_id
    from c_cte c
    inner join tac_cte tac on c.data_txn_acct_ctr_id = tac.data_acct_ctr_id
    inner join sac_cte sac on c.data_src_acct_ctr_id = sac.data_acct_ctr_id
)

-- select from the final result cte
select * from final