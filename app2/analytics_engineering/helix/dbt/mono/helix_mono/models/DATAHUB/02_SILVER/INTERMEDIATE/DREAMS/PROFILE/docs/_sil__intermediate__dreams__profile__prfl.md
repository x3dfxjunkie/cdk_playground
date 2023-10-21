{% docs sil__intermediate__dreams__profile__prfl_cleansed %}

#### Object Name
prfl_cleansed

#### Object Definition
This table provides coded comments across the dreams application for the following types

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_prfl_id & metadata_checksum combination.

#### Primary key
data_prfl_id

#### Tags
    - object_name=prfl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__profile__prfl_versioned %}

#### Object Name
prfl_versioned

#### Object Definition
This table provides coded comments across the dreams application for the following types

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_prfl_id & metadata_checksum combination.

#### Primary key
data_prfl_id

#### Tags
    - object_name=prfl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}