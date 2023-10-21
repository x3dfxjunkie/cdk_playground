with cmps_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__cmps_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

cmps_bus_org_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__cmps_bus_org_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

cmps_config_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__cmps_config_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

bus_org_acct_dt_cte as (
    select
        *
    from
        {{ ref('sil__intermediate__dreams__resource_inventory_management__bus_org_acct_dt_versioned') }}
    where
        metadata_version_end_datetime = '{{ var('metadata_version_end_date') }}'
        and upper(metadata_operation) != 'DELETE'
),

final as (
    select
        distinct c.data_cmps_id as campus_id,
        c.data_cmps_nm as campus_name,
        cbo.data_bus_org_id as business_organization_id,
        cbo.data_bus_org_nm as business_organization_name,
        boad.data_curr_acct_dt as current_account_date,
        cc.data_tm_zn_nm as time_zone_name,
        cc.data_byps_bal_due_in as bypass_balance_due_indicator,
        cc.data_dt_fmt_vl as date_format_value
    from
        cmps_cte as c
        inner join cmps_bus_org_cte as cbo
        on c.data_cmps_id = cbo.data_cmps_id
        inner join cmps_config_cte as cc
        on cbo.data_cmps_id = cc.data_cmps_id
        inner join bus_org_acct_dt_cte as boad
        on cbo.data_bus_org_id = boad.data_bus_org_id
)
select * from final
