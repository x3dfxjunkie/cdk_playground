{% docs sil__intermediate__travelbox__west__uda_applicable_value_cleansed %}

#### Object Name
uda_applicable_value_cleansed

#### Object Definition
User defined attribute values

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_applicable_value_id, data_attribute_id & metadata_checksum combination.

#### Primary key
data_applicable_value_id, data_attribute_id

#### Tags
    - object_name=uda_applicable_value
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__uda_applicable_value_versioned %}

#### Object Name
uda_applicable_value_versioned

#### Object Definition
User defined attribute values

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_applicable_value_id, data_attribute_id & metadata_checksum combination.

#### Primary key
data_applicable_value_id, data_attribute_id

#### Tags
    - object_name=uda_applicable_value
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}