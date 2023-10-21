{% docs sil__intermediate__dreams__dining__tps_alrgy_cleansed %}

#### Object Name
tps_alrgy_cleansed

#### Object Definition
This table ties an allergy type to a specific reservation

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_alrgy_id & metadata_checksum combination.

#### Primary key
data_alrgy_id

#### Tags
    - object_name=tps_alrgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__tps_alrgy_versioned %}

#### Object Name
tps_alrgy_versioned

#### Object Definition
This table ties an allergy type to a specific reservation

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_alrgy_id & metadata_checksum combination.

#### Primary key
data_alrgy_id

#### Tags
    - object_name=tps_alrgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}