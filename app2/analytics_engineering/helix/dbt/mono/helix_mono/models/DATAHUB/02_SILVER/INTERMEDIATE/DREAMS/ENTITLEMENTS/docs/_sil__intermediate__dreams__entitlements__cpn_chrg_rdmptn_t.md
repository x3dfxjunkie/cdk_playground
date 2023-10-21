{% docs sil__intermediate__dreams__entitlements__cpn_chrg_rdmptn_t_cleansed %}

#### Table Name
cpn_chrg_rdmptn_t_cleansed

#### Table Definition
This table associates the coupon charge to the Entitlement Plan providing the count of coupons redeemed

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cpn_rdmptn_id & metadata_checksum combination.

#### Primary key
data_cpn_rdmptn_id

#### Tags
    - table_name=cpn_chrg_rdmptn_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__cpn_chrg_rdmptn_t_versioned %}

#### Table Name
cpn_chrg_rdmptn_t_versioned

#### Table Definition
This table associates the coupon charge to the Entitlement Plan providing the count of coupons redeemed

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cpn_rdmptn_id & metadata_checksum combination.

#### Primary key
data_cpn_rdmptn_id

#### Tags
    - table_name=cpn_chrg_rdmptn_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}