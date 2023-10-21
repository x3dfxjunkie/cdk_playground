{% docs sil__intermediate__dreams__rooms_fulfillment__alrgy_cleansed %}

#### Object Name
alrgy_cleansed

#### Object Definition
This is table contains Food Allergies and descriptions

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_alrgy_id & metadata_checksum combination.

#### Primary key
data_alrgy_id

#### Tags
    - object_name=alrgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__alrgy_versioned %}

#### Object Name
alrgy_versioned

#### Object Definition
This is table contains Food Allergies and descriptions

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_alrgy_id & metadata_checksum combination.

#### Primary key
data_alrgy_id

#### Tags
    - object_name=alrgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}