{% docs sil__intermediate__das__wdw__enttl_updt_log_cleansed %}

#### Object Name
enttl_updt_log_cleansed

#### Object Definition
Audit table that logs which cast member users updated/created which DAS entitlements.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_log_id & metadata_checksum combination.

#### Primary key
data_log_id

#### Tags
    - object_name=enttl_updt_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__das__wdw__enttl_updt_log_versioned %}

#### Object Name
enttl_updt_log_versioned

#### Object Definition
Audit table that logs which cast member users updated/created which DAS entitlements.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_log_id & metadata_checksum combination.

#### Primary key
data_log_id

#### Tags
    - object_name=enttl_updt_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}