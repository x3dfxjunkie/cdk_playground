{% docs sil__intermediate__das__wdw__enttl_lnk_cleansed %}

#### Object Name
enttl_lnk_cleansed

#### Object Definition
Linkage table that contains relationship between the DAS entitlement and the Guest ID.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_enttl_id, data_lnk_id & metadata_checksum combination.

#### Primary key
data_enttl_id, data_lnk_id

#### Tags
    - object_name=enttl_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__das__wdw__enttl_lnk_versioned %}

#### Object Name
enttl_lnk_versioned

#### Object Definition
Linkage table that contains relationship between the DAS entitlement and the Guest ID.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_enttl_id, data_lnk_id & metadata_checksum combination.

#### Primary key
data_enttl_id, data_lnk_id

#### Tags
    - object_name=enttl_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}