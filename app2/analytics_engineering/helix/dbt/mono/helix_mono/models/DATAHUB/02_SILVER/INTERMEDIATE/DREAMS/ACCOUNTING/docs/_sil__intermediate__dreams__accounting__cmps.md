{% docs sil__intermediate__dreams__accounting__cmps_cleansed %}

#### Object Name
cmps_cleansed

#### Object Definition
The 3 areas that use the CAMPUS system: Pacific Region GMT-10, Walt Disney World, Disneyland

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cmps_id & metadata_checksum combination.

#### Primary key
data_cmps_id

#### Tags
    - object_name=cmps
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__cmps_versioned %}

#### Object Name
cmps_versioned

#### Object Definition
The 3 areas that use the CAMPUS system: Pacific Region GMT-10, Walt Disney World, Disneyland

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cmps_id & metadata_checksum combination.

#### Primary key
data_cmps_id

#### Tags
    - object_name=cmps
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}