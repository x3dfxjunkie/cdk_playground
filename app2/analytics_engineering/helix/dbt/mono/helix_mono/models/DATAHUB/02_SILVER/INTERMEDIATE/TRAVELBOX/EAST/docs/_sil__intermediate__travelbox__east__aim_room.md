{% docs sil__intermediate__travelbox__east__aim_room_cleansed %}

#### Object Name
aim_room_cleansed

#### Object Definition
Room Setup Data

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code, data_supplier_id & metadata_checksum combination.

#### Primary key
data_code, data_supplier_id

#### Tags
    - object_name=aim_room
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__aim_room_versioned %}

#### Object Name
aim_room_versioned

#### Object Definition
Room Setup Data

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code, data_supplier_id & metadata_checksum combination.

#### Primary key
data_code, data_supplier_id

#### Tags
    - object_name=aim_room
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}