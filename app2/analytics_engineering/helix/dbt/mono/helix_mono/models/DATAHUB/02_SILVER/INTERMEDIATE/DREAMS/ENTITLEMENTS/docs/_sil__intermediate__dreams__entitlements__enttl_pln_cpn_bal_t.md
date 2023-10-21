{% docs sil__intermediate__dreams__entitlements__enttl_pln_cpn_bal_t_cleansed %}

#### Table Name
enttl_pln_cpn_bal_t_cleansed

#### Table Definition
This table tracks the number of Coupons as they are posted against the Entitlement Plan

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_enttl_pln_id & metadata_checksum combination.

#### Primary key
data_enttl_pln_id

#### Tags
    - table_name=enttl_pln_cpn_bal_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__enttl_pln_cpn_bal_t_versioned %}

#### Table Name
enttl_pln_cpn_bal_t_versioned

#### Table Definition
This table tracks the number of Coupons as they are posted against the Entitlement Plan

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_enttl_pln_id & metadata_checksum combination.

#### Primary key
data_enttl_pln_id

#### Tags
    - table_name=enttl_pln_cpn_bal_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}