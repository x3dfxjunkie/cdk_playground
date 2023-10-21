{% docs sil__intermediate__dreams__entitlements__enttl_pln_ext_ref_t_cleansed %}

#### Table Name
enttl_pln_ext_ref_t_cleansed

#### Table Definition
This table ties the external reference from Reservation Management to the Entitlement Plan based on: ENTTL_EXT_REF_TYP_NM
        Facility
        Room
        Travel Plan
        Travel Component Grouping
        and
        ENTTL_EXTNL_SRC_NM
        DREAMS_TC
        DREAMS_TCG
        DREAMS_TP
        FACILITY_ID
        ROOM

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_enttl_plan_ext_ref_id & metadata_checksum combination.

#### Primary key
data_enttl_plan_ext_ref_id

#### Tags
    - table_name=enttl_pln_ext_ref_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__enttl_pln_ext_ref_t_versioned %}

#### Table Name
enttl_pln_ext_ref_t_versioned

#### Table Definition
This table ties the external reference from Reservation Management to the Entitlement Plan based on: ENTTL_EXT_REF_TYP_NM
        Facility
        Room
        Travel Plan
        Travel Component Grouping
        and
        ENTTL_EXTNL_SRC_NM
        DREAMS_TC
        DREAMS_TCG
        DREAMS_TP
        FACILITY_ID
        ROOM

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_enttl_plan_ext_ref_id & metadata_checksum combination.

#### Primary key
data_enttl_plan_ext_ref_id

#### Tags
    - table_name=enttl_pln_ext_ref_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}