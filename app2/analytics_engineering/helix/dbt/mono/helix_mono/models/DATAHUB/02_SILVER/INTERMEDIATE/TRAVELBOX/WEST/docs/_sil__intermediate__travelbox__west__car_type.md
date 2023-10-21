{% docs sil__intermediate__travelbox__west__car_type_cleansed %}

#### Object Name
car_type_cleansed

#### Object Definition
Contias car types, defined from the Car module -&gt;setup -&gt; Car types

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=car_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__car_type_versioned %}

#### Object Name
car_type_versioned

#### Object Definition
Contias car types, defined from the Car module -&gt;setup -&gt; Car types

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=car_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}