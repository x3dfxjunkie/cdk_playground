{% docs sil__intermediate__dreams__profile__prfl_rte_cleansed %}

#### Object Name
prfl_rte_cleansed

#### Object Definition
This table links the route the profile should take based on type.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_prfl_rte_id & metadata_checksum combination.

#### Primary key
data_prfl_rte_id

#### Tags
    - object_name=prfl_rte
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__profile__prfl_rte_versioned %}

#### Object Name
prfl_rte_versioned

#### Object Definition
This table links the route the profile should take based on type.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_prfl_rte_id & metadata_checksum combination.

#### Primary key
data_prfl_rte_id

#### Tags
    - object_name=prfl_rte
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}