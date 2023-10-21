{% docs sil__intermediate__dreams__entitlements__pos_cpn_chrg_t_cleansed %}

#### Table Name
pos_cpn_chrg_t_cleansed

#### Table Definition
This table ties the source POS charge ID to the Coupon charge ID to provide additional information about the source transaction.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pos_cpn_chrg_id & metadata_checksum combination.

#### Primary key
data_pos_cpn_chrg_id

#### Tags
    - table_name=pos_cpn_chrg_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__pos_cpn_chrg_t_versioned %}

#### Table Name
pos_cpn_chrg_t_versioned

#### Table Definition
This table ties the source POS charge ID to the Coupon charge ID to provide additional information about the source transaction.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pos_cpn_chrg_id & metadata_checksum combination.

#### Primary key
data_pos_cpn_chrg_id

#### Tags
    - table_name=pos_cpn_chrg_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}