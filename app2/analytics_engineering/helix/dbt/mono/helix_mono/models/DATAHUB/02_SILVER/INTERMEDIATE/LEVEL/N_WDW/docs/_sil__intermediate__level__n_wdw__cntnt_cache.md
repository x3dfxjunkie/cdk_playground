{% docs sil__intermediate__level__n_wdw__cntnt_cache_cleansed %}

#### Object Name
cntnt_cache_cleansed

#### Object Definition
Product information from the content management system.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cntnt_cache_id & metadata_checksum combination.

#### Primary key
data_cntnt_cache_id

#### Tags
    - object_name=cntnt_cache
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__cntnt_cache_versioned %}

#### Object Name
cntnt_cache_versioned

#### Object Definition
Product information from the content management system.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cntnt_cache_id & metadata_checksum combination.

#### Primary key
data_cntnt_cache_id

#### Tags
    - object_name=cntnt_cache
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}