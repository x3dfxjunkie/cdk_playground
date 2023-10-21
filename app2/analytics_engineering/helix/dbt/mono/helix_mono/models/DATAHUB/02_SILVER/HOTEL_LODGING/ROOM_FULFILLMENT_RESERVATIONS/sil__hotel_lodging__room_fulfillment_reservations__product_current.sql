-- create ctes for each table with select * to initially include all columns
with cte_p as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__prod_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),
cte_adm as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__adm_prod_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_tkt as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__tkt_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_tktf as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__tkt_feat_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_feat as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__feat_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_featp as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__feat_price_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_pad as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__cmpnt_prod_age_def_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_ad as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__age_def_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_arc as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__acct_rev_cls_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_fp as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__fac_prod_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_ap as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__acm_prod_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_pcls as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__prod_cls_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_pcp as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__prod_chan_prod_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
cte_pc as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__price__prod_chan_t_versioned') }}
	where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
		and upper(metadata_operation) != 'DELETE'
),
-- final cte selects specific columns from the ctes
final as (
    select
        p.data_prod_id as product_id,
        p.data_prod_cls_id as product_class_id,
        p.data_acct_rev_cls_id as account_revenue_class_id,
        pcls.data_prnt_prod_cls_id as parent_product_class_id,
        pcls.data_prod_cls_lvl_nb as product_class_level_number,
        pcls.data_prod_cls_nm as product_class_name,
        p.data_prod_yr_nb as product_year_number,
        p.data_prod_typ_nm as product_type_name,
        p.data_prod_cd as product_code,
        p.data_prod_intrnl_nm as product_internal_name,
        p.data_prod_intrnl_ds as product_internal_description,
        p.data_prod_bkng_strt_dts as product_booking_start_dts,
        p.data_prod_usg_strt_dts as product_usage_start_dts,
        fp.data_fac_prod_typ_nm as facility_product_type_name,
        fp.data_fac_id as facility_id,
        ap.data_acm_prod_id as acm_prod_id,
        ap.data_rm_typ_cd as rm_typ_cd,
        ap.data_acm_prod_addl_chg_thrshld_nb as acm_prod_addl_chg_thrshld_nb,
        null as entrprs_data_fac_id,
        null as data_fac_short_nm,
        tkt.data_tkt_cd as admission_ticket_code,
        arc.data_prnt_acct_rev_cls_id as parent_account_revenue_class_id,
        arc.data_acct_rev_cls_lvl_nb as account_revenue_class_level_number,
        arc.data_acct_rev_cls_nm as account_revenue_class_name,
        ad.data_age_typ_nm as age_type_name,
        ad.data_entrprs_age_typ_id as enterprise_age_type_id,
        ad.data_age_def_min_age_nb as age_default_min_age_nb,
        ad.data_age_def_max_age_nb as age_default_max_age_nb,
        ad.data_entrprs_age_typ_nm as enterprise_age_type_name,
        tkt.data_tkt_sls_strt_dt as ticket_sales_start_date,
        tkt.data_tkt_sls_end_dt as ticket_sales_end_date,
        adm.data_adm_dy_vld_cn as admission_day_valid_count,
        adm.data_adm_exp_dy_cn as admission_expiration_day_count,
        adm.data_adm_addtnl_ds as admission_additional_description,
        feat.data_feat_frq_nm as admission_feature_frequency_name,
        feat.data_feat_ds as admission_feature_description,
        feat.data_feat_nm as admission_feature_name,
        tkt.data_tkt_am as admission_ticket_amount,
        tkt.data_tkt_tax_am as admission_ticket_tax_amount,
        pcp.data_prod_chan_id as product_channel_id,
        pc.data_prod_chan_typ_nm as product_channel_type_name,
        pc.data_prod_chan_nm as product_channel_name,
        pc.data_prod_chan_strt_dt as product_channel_start_date,
        pc.data_prod_chan_end_dt as product_channel_end_date,
        pc.data_prod_chan_actv_in as product_channel_active_indicator,
        pc.data_prod_chan_rsr_in as product_channel_resort_special_reservation_indicator
    from
        cte_p p
        left join cte_adm adm
        on p.data_prod_id = adm.data_adm_prod_id
        left join cte_tkt tkt
        on adm.data_adm_prod_id = tkt.data_adm_prod_id
        left join cte_tktf tktf
        on tkt.data_tkt_id = tktf.data_tkt_id
        left join cte_feat feat
        on tktf.data_feat_id = feat.data_feat_id
        left join cte_featp featp
        on feat.data_feat_id = featp.data_feat_id
        left join cte_pad pad
        on pad.data_prod_id = p.data_prod_id
        left join cte_ad ad
        on pad.data_age_def_id = ad.data_age_def_id
        left join cte_arc arc
        on arc.data_acct_rev_cls_id = p.data_acct_rev_cls_id
        left join cte_fp fp
        on p.data_prod_id = fp.data_prod_id
        left join cte_ap ap
        on ap.data_acm_prod_id = fp.data_prod_id
        left join cte_pcls pcls
        on p.data_prod_cls_id = pcls.data_prod_cls_id
        left join cte_pcp pcp
        on p.data_prod_id = pcp.data_prod_id
        left join cte_pc pc
        on pcp.data_prod_chan_id = pc.data_prod_chan_id
)

select * from final