{% docs sil__intermediate__level__n_wdw__lvl_n_chng_cleansed %}

#### Object Name
lvl_n_chng_cleansed

#### Object Definition
Captures all changes for a Level N Entitlement - such as when the Guest changes their arrival date, or when the status of the entitlement changes.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_enttl_chng_dt, data_lvl_n_enttl_id & metadata_checksum combination.

#### Primary key
data_lvl_n_enttl_chng_dt, data_lvl_n_enttl_id

#### Tags
    - object_name=lvl_n_chng
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_chng_versioned %}

#### Object Name
lvl_n_chng_versioned

#### Object Definition
Captures all changes for a Level N Entitlement - such as when the Guest changes their arrival date, or when the status of the entitlement changes.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_enttl_chng_dt, data_lvl_n_enttl_id & metadata_checksum combination.

#### Primary key
data_lvl_n_enttl_chng_dt, data_lvl_n_enttl_id

#### Tags
    - object_name=lvl_n_chng
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}