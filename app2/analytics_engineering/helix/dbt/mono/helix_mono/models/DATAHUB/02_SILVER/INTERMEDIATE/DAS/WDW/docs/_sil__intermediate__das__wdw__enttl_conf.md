{% docs sil__intermediate__das__wdw__enttl_conf_cleansed %}

#### Object Name
enttl_conf_cleansed

#### Object Definition
Reference table on configuration short names and their descriptions for the DAS entitlements.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_conf_nm & metadata_checksum combination.

#### Primary key
data_conf_nm

#### Tags
    - object_name=enttl_conf
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__das__wdw__enttl_conf_versioned %}

#### Object Name
enttl_conf_versioned

#### Object Definition
Reference table on configuration short names and their descriptions for the DAS entitlements.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_conf_nm & metadata_checksum combination.

#### Primary key
data_conf_nm

#### Tags
    - object_name=enttl_conf
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}