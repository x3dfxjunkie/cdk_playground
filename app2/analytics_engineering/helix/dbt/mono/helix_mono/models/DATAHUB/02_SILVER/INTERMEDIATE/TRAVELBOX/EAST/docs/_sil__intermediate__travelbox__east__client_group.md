{% docs sil__intermediate__travelbox__east__client_group_cleansed %}

#### Object Name
client_group_cleansed

#### Object Definition
User defined client group code and name. Set up at Client Groups in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=client_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__client_group_versioned %}

#### Object Name
client_group_versioned

#### Object Definition
User defined client group code and name. Set up at Client Groups in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=client_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}