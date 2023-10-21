{% docs sil__intermediate__dreams__price__pkg_blk_out_sch_t_cleansed %}

#### Object Name
pkg_blk_out_sch_t_cleansed

#### Object Definition
This table provides the dates that a specific package is not available for booking

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pkg_blk_out_sch_strt_dt, data_pkg_id & metadata_checksum combination.

#### Primary key
data_pkg_blk_out_sch_strt_dt, data_pkg_id

#### Tags
    - object_name=pkg_blk_out_sch_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__pkg_blk_out_sch_t_versioned %}

#### Object Name
pkg_blk_out_sch_t_versioned

#### Object Definition
This table provides the dates that a specific package is not available for booking

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pkg_blk_out_sch_strt_dt, data_pkg_id & metadata_checksum combination.

#### Primary key
data_pkg_blk_out_sch_strt_dt, data_pkg_id

#### Tags
    - object_name=pkg_blk_out_sch_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}