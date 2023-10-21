{% docs sil__intermediate__dreams__entitlements__cpn_pos_loc_config_t_cleansed %}

#### Table Name
cpn_pos_loc_config_t_cleansed

#### Table Definition
This table associates Transaction Center Account IDs to Sales locations via Register Number Value this provides the configuration to know if a coupon charge is allowed to be accepted and/or reposted

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cpn_pos_loc_config_id & metadata_checksum combination.

#### Primary key
data_cpn_pos_loc_config_id

#### Tags
    - table_name=cpn_pos_loc_config_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__cpn_pos_loc_config_t_versioned %}

#### Table Name
cpn_pos_loc_config_t_versioned

#### Table Definition
This table associates Transaction Center Account IDs to Sales locations via Register Number Value this provides the configuration to know if a coupon charge is allowed to be accepted and/or reposted

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cpn_pos_loc_config_id & metadata_checksum combination.

#### Primary key
data_cpn_pos_loc_config_id

#### Tags
    - table_name=cpn_pos_loc_config_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}