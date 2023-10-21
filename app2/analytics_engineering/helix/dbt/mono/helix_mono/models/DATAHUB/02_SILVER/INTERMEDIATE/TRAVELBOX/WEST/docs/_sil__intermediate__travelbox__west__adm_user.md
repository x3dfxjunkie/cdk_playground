{% docs sil__intermediate__travelbox__west__adm_user_cleansed %}

#### Object Name
adm_user_cleansed

#### Object Definition
User profiles for the cast members using Travelbox

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_user_id & metadata_checksum combination.

#### Primary key
data_user_id

#### Tags
    - object_name=adm_user
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__adm_user_versioned %}

#### Object Name
adm_user_versioned

#### Object Definition
User profiles for the cast members using Travelbox

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_user_id & metadata_checksum combination.

#### Primary key
data_user_id

#### Tags
    - object_name=adm_user
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}