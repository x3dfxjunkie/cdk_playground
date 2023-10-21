{% docs sil__intermediate__dreams__group_management__grp_cleansed %}

#### Object Name
grp_cleansed

#### Object Definition
Information related to the group based on the profile created by the group office

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_grp_cd & metadata_checksum combination.

#### Primary key
data_grp_cd

#### Tags
    - object_name=grp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__grp_versioned %}

#### Object Name
grp_versioned

#### Object Definition
Information related to the group based on the profile created by the group office

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_grp_cd & metadata_checksum combination.

#### Primary key
data_grp_cd

#### Tags
    - object_name=grp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}