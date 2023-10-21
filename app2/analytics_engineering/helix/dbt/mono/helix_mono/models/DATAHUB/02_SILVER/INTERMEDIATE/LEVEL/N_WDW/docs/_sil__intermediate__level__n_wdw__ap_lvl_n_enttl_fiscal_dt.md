{% docs sil__intermediate__level__n_wdw__ap_lvl_n_enttl_fiscal_dt_cleansed %}

#### Object Name
ap_lvl_n_enttl_fiscal_dt_cleansed

#### Object Definition
Contains information about the fiscal date of the revenue realized for the level n entitlement for annual passholders.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_rvn_fiscal_dt_id & metadata_checksum combination.

#### Primary key
data_lvl_n_rvn_fiscal_dt_id

#### Tags
    - object_name=ap_lvl_n_enttl_fiscal_dt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__ap_lvl_n_enttl_fiscal_dt_versioned %}

#### Object Name
ap_lvl_n_enttl_fiscal_dt_versioned

#### Object Definition
Contains information about the fiscal date of the revenue realized for the level n entitlement for annual passholders.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_rvn_fiscal_dt_id & metadata_checksum combination.

#### Primary key
data_lvl_n_rvn_fiscal_dt_id

#### Tags
    - object_name=ap_lvl_n_enttl_fiscal_dt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}