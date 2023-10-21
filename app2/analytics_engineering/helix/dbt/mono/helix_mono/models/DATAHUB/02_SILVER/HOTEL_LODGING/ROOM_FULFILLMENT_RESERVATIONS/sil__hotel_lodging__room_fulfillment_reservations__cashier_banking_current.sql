with bi_cte as (

    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__bank_in_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
bo_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__bank_out_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
bac_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__bank_acct_ctr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
ds_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__dsny_sys_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
ac_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__acct_ctr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
final_cte as (
    select
        distinct bi.data_bank_in_id as bank_in_id,
        bi.data_bank_in_acct_dt as bank_in_account_date,
        bi.data_bank_in_dts as bank_in_date_time,
        bi.data_bank_acct_ctr_id as bank_account_center_id,
        ac.data_acct_ctr_nm as account_center_name,
        bo.data_bank_out_id as bank_out_id,
        bo.data_bank_out_typ_nm as bank_out_type_name,
        bo.data_bank_out_acct_dt as bank_out_account_date,
        bo.data_dpst_bag_id as deposit_bag_id,
        bo.data_bank_out_comp_dts as bank_out_completed_date_time,
        bo.data_rgstr_am as register_amount,
        bac.data_dsny_sys_cd as disney_system_code,
        ds.data_dsny_sys_nm as disney_system_name,
        bac.data_tcr_loc_in as tcr_location_indicator,
        bac.data_gst_fc_in as guest_facing_indicator,
        bac.data_bank_out_in as data_bank_out_indicator,
        bac.data_ovr_shrt_csh_am as over_short_cash_amount,
        bac.data_ovr_shrt_crncy_cd as over_short_currency_code,
        bac.data_barcd_prt_in as barcode_print_indicator,
        bac.data_till_dspns_in as till_dispensed_indicator,
        bac.data_strts_term_nb as stratus_terminal_number,
        bac.data_rgstr_nb_vl as register_number_value
    from
        bi_cte bi
        inner join bo_cte bo
        on bi.data_bank_in_id = bo.data_bank_in_id
        left join bac_cte bac
        on bi.data_bank_acct_ctr_id = bac.data_bank_acct_ctr_id
        left join ds_cte ds
        on bac.data_dsny_sys_cd = ds.data_dsny_sys_cd
        left join ac_cte ac
        on bac.data_acct_ctr_id = ac.data_acct_ctr_id
)
select
    *
from
    final_cte
