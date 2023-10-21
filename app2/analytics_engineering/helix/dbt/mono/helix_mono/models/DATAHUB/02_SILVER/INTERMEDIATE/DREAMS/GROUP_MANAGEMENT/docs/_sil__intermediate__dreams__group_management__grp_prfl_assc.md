{% docs sil__intermediate__dreams__group_management__grp_prfl_assc_cleansed %}

#### Object Name
grp_prfl_assc_cleansed

#### Object Definition
Last Load 06/16/2015

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_grp_prfl_assc_id & metadata_checksum combination.

#### Primary key
data_grp_prfl_assc_id

#### Tags
    - object_name=grp_prfl_assc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__grp_prfl_assc_versioned %}

#### Object Name
grp_prfl_assc_versioned

#### Object Definition
Last Load 06/16/2015

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_grp_prfl_assc_id & metadata_checksum combination.

#### Primary key
data_grp_prfl_assc_id

#### Tags
    - object_name=grp_prfl_assc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}