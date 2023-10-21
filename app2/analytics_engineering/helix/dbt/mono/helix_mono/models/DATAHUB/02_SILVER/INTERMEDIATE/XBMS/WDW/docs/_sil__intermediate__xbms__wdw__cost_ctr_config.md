{% docs sil__intermediate__xbms__wdw__cost_ctr_config_cleansed %}

#### Object Name
cost_ctr_config_cleansed

#### Object Definition
Reference table for cost center config and their attributes such as disney facility id.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cost_ctr_config_id & metadata_checksum combination.

#### Primary key
data_cost_ctr_config_id

#### Tags
    - object_name=cost_ctr_config
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__cost_ctr_config_versioned %}

#### Object Name
cost_ctr_config_versioned

#### Object Definition
Reference table for cost center config and their attributes such as disney facility id.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cost_ctr_config_id & metadata_checksum combination.

#### Primary key
data_cost_ctr_config_id

#### Tags
    - object_name=cost_ctr_config
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}