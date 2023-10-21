{% docs sil__intermediate__dreams__entitlements__chrg_item_t_cleansed %}

#### Table Name
chrg_item_t_cleansed

#### Table Definition
Provides information regarding the Coupon Charge, down at the item level

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrg_item_id & metadata_checksum combination.

#### Primary key
data_chrg_item_id

#### Tags
    - table_name=chrg_item_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__chrg_item_t_versioned %}

#### Table Name
chrg_item_t_versioned

#### Table Definition
Provides information regarding the Coupon Charge, down at the item level

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrg_item_id & metadata_checksum combination.

#### Primary key
data_chrg_item_id

#### Tags
    - table_name=chrg_item_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}