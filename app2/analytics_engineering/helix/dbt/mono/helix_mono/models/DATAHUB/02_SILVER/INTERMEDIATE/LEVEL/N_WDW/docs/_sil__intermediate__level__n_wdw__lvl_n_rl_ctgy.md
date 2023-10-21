{% docs sil__intermediate__level__n_wdw__lvl_n_rl_ctgy_cleansed %}

#### Object Name
lvl_n_rl_ctgy_cleansed

#### Object Definition
A higher level of classification of roles for grouping purposes. Examples are: Guest, Cast Member

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_rl_ctgy_id & metadata_checksum combination.

#### Primary key
data_lvl_n_rl_ctgy_id

#### Tags
    - object_name=lvl_n_rl_ctgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_rl_ctgy_versioned %}

#### Object Name
lvl_n_rl_ctgy_versioned

#### Object Definition
A higher level of classification of roles for grouping purposes. Examples are: Guest, Cast Member

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_rl_ctgy_id & metadata_checksum combination.

#### Primary key
data_lvl_n_rl_ctgy_id

#### Tags
    - object_name=lvl_n_rl_ctgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}