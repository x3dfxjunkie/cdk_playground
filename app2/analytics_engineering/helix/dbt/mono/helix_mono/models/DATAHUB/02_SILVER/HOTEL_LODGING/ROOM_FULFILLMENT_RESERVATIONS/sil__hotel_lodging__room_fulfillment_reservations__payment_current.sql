-- define a cte for pmt
with pmt_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__pmt_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

-- define a cte for fi
fi_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__folio_item_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

-- define a cte for ac
ac_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__accounting__acct_ctr_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

-- join ctes to get the final result
final as(
select
    pmt.data_pmt_id as payment_id,
    pmt.data_bank_acct_ctr_id as bank_account_center_id,
    ac.data_acct_ctr_nm as bank_account_center_name,
    pmt.data_pmt_ref_vl as payment_reference_value,
    fi.data_folio_id as folio_id,
    fi.data_folio_item_id as folio_item_id,
    fi.data_folio_item_typ_nm as folio_item_type_name,
    fi.data_folio_item_am as data_folio_item_amount,
    pmt.data_tndr_am as tender_amount,
    pmt.data_pmt_dts as payment_datetime,
    to_date(data_pmt_dts) as payment_date,
    pmt.data_acct_dt as account_date,
    pmt.data_pmt_pst_dts as payment_post_datetime,
    to_date(data_pmt_pst_dts) as payment_post_date,
    pmt.data_recog_sts_nm as regognition_status_name,
    pmt.data_pmt_meth_nm as payment_method_name,
    pmt.data_pmt_meth_typ_nm as payment_method_type_name,
    pmt.data_folio_txn_typ_cd as folio_transaction_type_code,
    pmt.data_pmt_pst_st_nm as payment_post_state_name,
    pmt.data_bank_in_id as bank_in_id,
    pmt.data_tndr_crncy_cd as tender_currency_code,
    pmt.data_pmt_exchg_rt as payment_exchange_rate,
    pmt.data_sprs_pmt_id as supress_payment_id,
    pmt.data_ovrd_rfnd_pmt_meth_in as override_refund_payment_method_indicator,
    pmt.data_wrk_loc_id as work_location_id,
    pmt.data_appl_by_nm as applied_by_name,
    fi.data_create_dts as create_datetime,
    to_date(fi.data_create_dts) as create_date,
    fi.data_create_usr_id_cd as create_user_id,
    fi.data_updt_dts as source_update_datetime,
    to_date(fi.data_updt_dts) as source_system_update_date,
    fi.data_updt_usr_id_cd as source_update_user_id
from
    pmt_cte pmt
    inner join fi_cte fi
    on pmt.data_folio_item_id = fi.data_folio_item_id
    inner join ac_cte ac
    on pmt.data_bank_acct_ctr_id = ac.data_acct_ctr_id
)

-- select from the final result cte
select * from final
