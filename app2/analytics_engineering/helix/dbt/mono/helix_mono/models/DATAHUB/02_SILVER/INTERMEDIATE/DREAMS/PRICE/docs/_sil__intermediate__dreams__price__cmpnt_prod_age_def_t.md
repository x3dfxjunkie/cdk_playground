{% docs sil__intermediate__dreams__price__cmpnt_prod_age_def_t_cleansed %}

#### Object Name
cmpnt_prod_age_def_t_cleansed

#### Object Definition
Ties the age definition ID to the product ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_age_def_id, data_prod_id & metadata_checksum combination.

#### Primary key
data_age_def_id, data_prod_id

#### Tags
    - object_name=cmpnt_prod_age_def_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__cmpnt_prod_age_def_t_versioned %}

#### Object Name
cmpnt_prod_age_def_t_versioned

#### Object Definition
Ties the age definition ID to the product ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_age_def_id, data_prod_id & metadata_checksum combination.

#### Primary key
data_age_def_id, data_prod_id

#### Tags
    - object_name=cmpnt_prod_age_def_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}