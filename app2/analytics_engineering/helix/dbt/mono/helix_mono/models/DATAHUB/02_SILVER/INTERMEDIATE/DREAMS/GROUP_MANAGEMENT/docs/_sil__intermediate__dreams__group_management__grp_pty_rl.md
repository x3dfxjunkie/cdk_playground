{% docs sil__intermediate__dreams__group_management__grp_pty_rl_cleansed %}

#### Object Name
grp_pty_rl_cleansed

#### Object Definition
This table associates a Group Code to a Party ID by role type, ie: Primary Contact, Speaker, etc

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_grp_cd, data_pty_id & metadata_checksum combination.

#### Primary key
data_grp_cd, data_pty_id

#### Tags
    - object_name=grp_pty_rl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__grp_pty_rl_versioned %}

#### Object Name
grp_pty_rl_versioned

#### Object Definition
This table associates a Group Code to a Party ID by role type, ie: Primary Contact, Speaker, etc

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_grp_cd, data_pty_id & metadata_checksum combination.

#### Primary key
data_grp_cd, data_pty_id

#### Tags
    - object_name=grp_pty_rl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}