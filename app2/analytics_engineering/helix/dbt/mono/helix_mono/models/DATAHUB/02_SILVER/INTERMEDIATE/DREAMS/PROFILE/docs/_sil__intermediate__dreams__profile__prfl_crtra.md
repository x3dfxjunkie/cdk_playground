{% docs sil__intermediate__dreams__profile__prfl_crtra_cleansed %}

#### Object Name
prfl_crtra_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_prfl_crtra_id & metadata_checksum combination.

#### Primary key
data_prfl_crtra_id

#### Tags
    - object_name=prfl_crtra
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__profile__prfl_crtra_versioned %}

#### Object Name
prfl_crtra_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_prfl_crtra_id & metadata_checksum combination.

#### Primary key
data_prfl_crtra_id

#### Tags
    - object_name=prfl_crtra
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}