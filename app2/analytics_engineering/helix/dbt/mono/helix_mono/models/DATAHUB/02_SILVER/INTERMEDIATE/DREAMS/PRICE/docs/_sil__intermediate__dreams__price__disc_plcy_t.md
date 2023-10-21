{% docs sil__intermediate__dreams__price__disc_plcy_t_cleansed %}

#### Object Name
disc_plcy_t_cleansed

#### Object Definition
Subset of policies that apply to products

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_disc_plcy_id & metadata_checksum combination.

#### Primary key
data_disc_plcy_id

#### Tags
    - object_name=disc_plcy_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__disc_plcy_t_versioned %}

#### Object Name
disc_plcy_t_versioned

#### Object Definition
Subset of policies that apply to products

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_disc_plcy_id & metadata_checksum combination.

#### Primary key
data_disc_plcy_id

#### Tags
    - object_name=disc_plcy_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}