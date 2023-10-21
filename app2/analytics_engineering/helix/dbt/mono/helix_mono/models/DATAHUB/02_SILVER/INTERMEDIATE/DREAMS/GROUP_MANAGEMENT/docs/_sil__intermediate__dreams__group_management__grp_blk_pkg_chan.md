{% docs sil__intermediate__dreams__group_management__grp_blk_pkg_chan_cleansed %}

#### Object Name
grp_blk_pkg_chan_cleansed

#### Object Definition
Last Load 01/21/2022

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_blk_cd & metadata_checksum combination.

#### Primary key
data_blk_cd

#### Tags
    - object_name=grp_blk_pkg_chan
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__grp_blk_pkg_chan_versioned %}

#### Object Name
grp_blk_pkg_chan_versioned

#### Object Definition
Last Load 01/21/2022

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_blk_cd & metadata_checksum combination.

#### Primary key
data_blk_cd

#### Tags
    - object_name=grp_blk_pkg_chan
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}