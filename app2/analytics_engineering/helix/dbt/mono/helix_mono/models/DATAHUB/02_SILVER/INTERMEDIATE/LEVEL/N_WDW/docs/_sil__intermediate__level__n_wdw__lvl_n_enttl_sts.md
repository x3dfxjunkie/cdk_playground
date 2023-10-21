{% docs sil__intermediate__level__n_wdw__lvl_n_enttl_sts_cleansed %}

#### Object Name
lvl_n_enttl_sts_cleansed

#### Object Definition
A collection of the values for lifecycle changes on the Memory Maker entitlements.  Values include:  created
active
cancelled
expired
consumed
reserved

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_enttl_sts_id & metadata_checksum combination.

#### Primary key
data_lvl_n_enttl_sts_id

#### Tags
    - object_name=lvl_n_enttl_sts
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_enttl_sts_versioned %}

#### Object Name
lvl_n_enttl_sts_versioned

#### Object Definition
A collection of the values for lifecycle changes on the Memory Maker entitlements.  Values include:  created
active
cancelled
expired
consumed
reserved

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_enttl_sts_id & metadata_checksum combination.

#### Primary key
data_lvl_n_enttl_sts_id

#### Tags
    - object_name=lvl_n_enttl_sts
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}