{% docs sil__intermediate__dreams__accounting__pst_grp_alloc_cleansed %}

#### Object Name
pst_grp_alloc_cleansed

#### Object Definition
Post Group and Post Accounts associated to the allocation percentage for a specific time frame

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pst_grp_alloc_id & metadata_checksum combination.

#### Primary key
data_pst_grp_alloc_id

#### Tags
    - object_name=pst_grp_alloc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__pst_grp_alloc_versioned %}

#### Object Name
pst_grp_alloc_versioned

#### Object Definition
Post Group and Post Accounts associated to the allocation percentage for a specific time frame

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pst_grp_alloc_id & metadata_checksum combination.

#### Primary key
data_pst_grp_alloc_id

#### Tags
    - object_name=pst_grp_alloc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}