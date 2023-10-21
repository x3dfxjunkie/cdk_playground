with cgf_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_grp_folio_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
folio_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__folio_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
rcg_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__root_chrg_grp_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cgfs_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__chrg_grp_fol_smth_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
fco_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__folio_chkot_opt_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
fte_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__folio_tax_exmpt_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
final_cte as (
    select
        distinct cgf.data_chrg_grp_folio_id as data_folio_id,
        cgf.data_prmy_folio_in as primary_folio_indicator,
        cgf.data_root_chrg_grp_id as root_charge_group_id,
        cgf.data_folio_acct_typ_nm as folio_account_type_name,
        folio.data_folio_typ_nm as folio_type_name,
        folio.data_src_acct_ctr_id as source_account_center_id,
        cgf.data_folio_sts_nm as folio_status_name,
        rcg.data_trvl_agt_id as travel_agency_id,
        cgf.data_dflt_chrg_grp_id as default_charge_group_id,
        cgfs.data_settl_meth_id as settlement_method_id,
        cgf.data_chrg_grp_folio_strt_dt as charge_group_folio_start_date,
        cgf.data_chrg_grp_folio_end_dt as charge_group_folio_end_date,
        cgf.data_respb_pty_id as responsible_party_id,
        cgf.data_bill_pty_id as bill_party_id,
        cgf.data_prmy_pty_gst_nm as primary_party_guest_name,
        fco.data_chkot_opt_typ_nm as checkout_option_type_name,
        fco.data_txn_pty_lctr_id as transaction_party_locator_id,
        cgf.data_tax_exmpt_id as tax_exempt_id,
        fte.data_tax_exmpt_typ_nm as tax_exempt_type_name,
        fte.data_tax_exmpt_cert_nb_val as tax_exempt_certificate_number,
        cgf.data_sml_bal_wrtoff_in as small_balance_writeoff_indicator,
        cgf.data_folio_acct_lim_am as folio_account_limit_amount,
        cgf.data_folio_acct_lim_crncy_cd as folio_account_limit_currency_code,
        cgf.data_folio_actv_in as folio_active_indicator,
        cgf.data_onsite_in as data_onsite_indicator,
        cgf.data_pmt_ownr_in as payment_owner_indicator,
        cgf.data_zero_bal_verif_in as zero_balance_verify_indicator,
        cgf.data_settl_frq_typ_nm as settlement_frequency_type_name,
        cgf.data_create_usr_id_cd as create_user_id,
        cgf.data_create_dts as create_datetime,
        to_date(
            cgf.data_create_dts
        ) as create_date,
        cgf.data_updt_usr_id_cd as update_user_id,
        cgf.data_updt_dts as source_update_datetime,
        to_date(
            cgf.data_updt_dts
        ) as source_update_date
    from
        cgf_cte cgf
        inner join folio_cte folio
        on cgf.data_chrg_grp_folio_id = folio.data_folio_id
        inner join rcg_cte rcg
        on cgf.data_root_chrg_grp_id = rcg.data_root_chrg_grp_id
        left join cgfs_cte cgfs
        on cgf.data_chrg_grp_folio_id = cgfs.data_chrg_grp_folio_id
        left join fco_cte fco
        on cgf.data_chrg_grp_folio_id = fco.data_chrg_grp_folio_id
        left join fte_cte fte
        on cgf.data_tax_exmpt_id = fte.data_tax_exmpt_id
)
select
    *
from
    final_cte
