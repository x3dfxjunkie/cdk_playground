{% docs sil__intermediate__travelbox__west__fee_type_cleansed %}

#### Object Name
fee_type_cleansed

#### Object Definition
Additional fee types that will be automatically added to the booking if the specified fee application criteria matches the booking criteria. Set up at &#39;Fee types&#39; under General menu in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=fee_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__fee_type_versioned %}

#### Object Name
fee_type_versioned

#### Object Definition
Additional fee types that will be automatically added to the booking if the specified fee application criteria matches the booking criteria. Set up at &#39;Fee types&#39; under General menu in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=fee_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}