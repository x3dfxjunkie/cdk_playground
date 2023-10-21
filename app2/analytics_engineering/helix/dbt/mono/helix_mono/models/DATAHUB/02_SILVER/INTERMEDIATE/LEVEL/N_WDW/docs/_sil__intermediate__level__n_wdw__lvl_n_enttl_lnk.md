{% docs sil__intermediate__level__n_wdw__lvl_n_enttl_lnk_cleansed %}

#### Object Name
lvl_n_enttl_lnk_cleansed

#### Object Definition
Associates the Memory Maker Guest with his entitlement(s). A guest is allowed to have more than one entitlement, and an entitlement is allowed to have more than one Guest.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_enttl_id, data_lvl_n_enttl_lnk_strt_dt, data_lvl_n_lnk_id, data_lvl_n_rl_id & metadata_checksum combination.

#### Primary key
data_lvl_n_enttl_id, data_lvl_n_enttl_lnk_strt_dt, data_lvl_n_lnk_id, data_lvl_n_rl_id

#### Tags
    - object_name=lvl_n_enttl_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_enttl_lnk_versioned %}

#### Object Name
lvl_n_enttl_lnk_versioned

#### Object Definition
Associates the Memory Maker Guest with his entitlement(s). A guest is allowed to have more than one entitlement, and an entitlement is allowed to have more than one Guest.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_enttl_id, data_lvl_n_enttl_lnk_strt_dt, data_lvl_n_lnk_id, data_lvl_n_rl_id & metadata_checksum combination.

#### Primary key
data_lvl_n_enttl_id, data_lvl_n_enttl_lnk_strt_dt, data_lvl_n_lnk_id, data_lvl_n_rl_id

#### Tags
    - object_name=lvl_n_enttl_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}