{% docs sil__intermediate__dreams__dining__grp_tm_cleansed %}

#### Object Name
grp_tm_cleansed

#### Object Definition
This table provides the Group Team Name (or just the group name, if it&#39;s not a sporting event)

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_grp_tm_id & metadata_checksum combination.

#### Primary key
data_grp_tm_id

#### Tags
    - object_name=grp_tm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__grp_tm_versioned %}

#### Object Name
grp_tm_versioned

#### Object Definition
This table provides the Group Team Name (or just the group name, if it&#39;s not a sporting event)

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_grp_tm_id & metadata_checksum combination.

#### Primary key
data_grp_tm_id

#### Tags
    - object_name=grp_tm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}