{% docs sil__intermediate__level__n_wdw__lvl_n_lnk_assc_cleansed %}

#### Object Name
lvl_n_lnk_assc_cleansed

#### Object Definition
Tracks the Source System Guest Identifier (Level N Link ID) merges over time. When an identifier is replaced with another one, the source system logs that change in this table.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_accs_lvl_n_lnk_id, data_lvl_n_lnk_assc_strt_dt, data_lvl_n_lnk_id & metadata_checksum combination.

#### Primary key
data_accs_lvl_n_lnk_id, data_lvl_n_lnk_assc_strt_dt, data_lvl_n_lnk_id

#### Tags
    - object_name=lvl_n_lnk_assc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_lnk_assc_versioned %}

#### Object Name
lvl_n_lnk_assc_versioned

#### Object Definition
Tracks the Source System Guest Identifier (Level N Link ID) merges over time. When an identifier is replaced with another one, the source system logs that change in this table.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_accs_lvl_n_lnk_id, data_lvl_n_lnk_assc_strt_dt, data_lvl_n_lnk_id & metadata_checksum combination.

#### Primary key
data_accs_lvl_n_lnk_id, data_lvl_n_lnk_assc_strt_dt, data_lvl_n_lnk_id

#### Tags
    - object_name=lvl_n_lnk_assc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}