{% docs sil__intermediate__dreams__dining__tps_cleansed %}

#### Object Name
tps_cleansed

#### Object Definition
This is the reservation level of the Travel Plan, the Travel Plan segment which contains information about your travel dates, contact name, ID for the travel agencies and agents, travel status, etc

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tps_id & metadata_checksum combination.

#### Primary key
data_tps_id

#### Tags
    - object_name=tps
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__tps_versioned %}

#### Object Name
tps_versioned

#### Object Definition
This is the reservation level of the Travel Plan, the Travel Plan segment which contains information about your travel dates, contact name, ID for the travel agencies and agents, travel status, etc

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tps_id & metadata_checksum combination.

#### Primary key
data_tps_id

#### Tags
    - object_name=tps
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}