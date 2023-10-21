-- define a cte for tip
with tip_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_idvl_pty_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for tp
tp_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for tpr
tpr_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_pty_rl_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- define a cte for tipm
tipm_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__guest__txn_idvl_pty_mbshp_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
-- join tip, tp, tpr and tipm ctes to get the final result
final as (
    select
        tip.data_txn_idvl_pty_id as transaction_individual_party_id,
        tp.data_txn_pty_id as transaction_party_id,
        tp.data_txn_pty_typ_nm as transaction_party_type_name,
        tip.data_idvl_pty_actv_in as individual_party_active_indicator,
        tpr.data_pty_rl_nm as party_role_name,
        tip.data_salut_cd as salutation_code,
        tip.data_idvl_fst_nm as first_name,
        tip.data_idvl_lst_nm as last_name,
        tip.data_idvl_mid_nm as middle_name,
        tip.data_sfx_cd as suffix_code,
        tip.data_age_nb as age_number,
        tip.data_pos_lst_nm_cd as pos_last_name_code,
        tip.data_dvc_mbr_typ_nm as disney_vacaction_club_type_name,
        tip.data_dcl_txfr_cd as disney_cruise_line_transfer_code,
        tipm.data_mbrshp_id as membership,
        tipm.data_plcy_id as policy_id,
        tipm.data_prod_chan_id as product_channel_id
    from
        tip_cte tip
        left join tp_cte tp
        on tip.data_txn_idvl_pty_id = tp.data_txn_pty_id
        left join tpr_cte tpr
        on tp.data_txn_pty_id = tpr.data_txn_pty_id
        left join tipm_cte tipm
        on tip.data_txn_idvl_pty_id = tipm.data_txn_idvl_pty_id
) -- select from the final result cte
select
    *
from
    final
