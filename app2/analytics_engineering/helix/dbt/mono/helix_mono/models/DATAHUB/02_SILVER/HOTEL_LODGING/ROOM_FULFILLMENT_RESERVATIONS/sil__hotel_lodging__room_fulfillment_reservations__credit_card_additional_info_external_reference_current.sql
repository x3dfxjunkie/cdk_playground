-- define a cte for pc
with pc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__pmt_card_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for cp
cp_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__card_pmt_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for smc
smc_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__settl_meth_card_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for ca
ca_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__folio__card_auth_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- join ctes to get the final result
final as (
    select
        distinct pc.data_pmt_card_id as payment_card_id,
        cp.data_pmt_id as payment_id,
        smc.data_settl_meth_id as settlement_method_id,
        pc.data_pmt_card_brnd_nm as payment_card_brand_name,
        pc.data_strts_rtrv_ref_nb as stratus_retrieval_reference_number,
        pc.data_umsk_card_nb as partial_masked_card_number,
        pc.data_pmt_card_hld_nm as payment_card_holder_name,
        pc.data_pmt_card_hld_addr_ln1_vl as payment_card_holder_address_line_1_value,
        pc.data_pmt_card_hld_addr_ln2_vl as payment_card_holder_address_line_2_value,
        pc.data_pmt_card_hld_cty_nm as payment_card_holder_city_name,
        pc.data_pmt_card_hld_rgn_cd as payment_card_holder_region_code,
        pc.data_pmt_card_hld_rgn_nm as payment_card_holder_region_name,
        pc.data_pmt_card_hld_pstl_cd as payment_card_holder_postal_code,
        pc.data_pmt_card_hld_cntry_cd as payment_card_holder_country_code,
        pc.data_rrn_key_nb as rrn_key_nb,
        pc.data_pmt_crd_use_sts_nm as payment_card_use_status_name,
        pc.data_pmt_dev_trmnl_id as payment_device_terminal_id,
        ca.data_strts_card_cls_cd as stratus_card_class_code,
        ca.data_card_auth_cd as card_authorization_code,
        ca.data_cc_mrcht_nb as credit_card_merchant_number,
        ca.data_avs_resp_cd as avs_resp_cd,
        ca.data_strts_auth_typ_nm as stratus_authorization_type_name,
        ca.data_pmt_man_auth_in as payment_manual_authorization_indicator,
        ca.data_visa_auth_chrctr_cd as visa_authorization_character_code,
        ca.data_visa_txn_id as visa_transaction_id,
        ca.data_visa_vld_cd as visa_valid_code,
        ca.data_mc_bnknt_dt as mc_bnknt_dt,
        ca.data_cc_mrcht_ctgy_nb as credit_card_merchant_category_number,
        pc.data_create_usr_id_cd as create_user_id,
        pc.data_create_dts as create_datetime,
        to_date(
            pc.data_create_dts
        ) as create_date
    from
        pc_cte pc
        left join cp_cte cp
        on cp.data_pmt_card_id = pc.data_pmt_card_id
        left join smc_cte smc
        on pc.data_pmt_card_id = smc.data_pmt_card_id
        left join ca_cte ca
        on pc.data_pmt_card_id = ca.data_pmt_card_id
) 

-- select from the final result cte
select
    *
from
    final
