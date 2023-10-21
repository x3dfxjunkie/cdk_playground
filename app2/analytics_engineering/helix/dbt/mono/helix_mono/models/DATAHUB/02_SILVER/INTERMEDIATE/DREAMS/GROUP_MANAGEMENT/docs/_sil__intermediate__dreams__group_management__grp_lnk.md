{% docs sil__intermediate__dreams__group_management__grp_lnk_cleansed %}

#### Object Name
grp_lnk_cleansed

#### Object Definition
Last load 06-18-2019

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_prmy_grp_cd, data_sec_grp_cd & metadata_checksum combination.

#### Primary key
data_prmy_grp_cd, data_sec_grp_cd

#### Tags
    - object_name=grp_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__grp_lnk_versioned %}

#### Object Name
grp_lnk_versioned

#### Object Definition
Last load 06-18-2019

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_prmy_grp_cd, data_sec_grp_cd & metadata_checksum combination.

#### Primary key
data_prmy_grp_cd, data_sec_grp_cd

#### Tags
    - object_name=grp_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}