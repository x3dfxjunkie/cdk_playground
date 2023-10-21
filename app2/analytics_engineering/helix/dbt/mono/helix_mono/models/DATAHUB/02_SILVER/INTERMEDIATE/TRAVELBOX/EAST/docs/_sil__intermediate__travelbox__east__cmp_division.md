{% docs sil__intermediate__travelbox__east__cmp_division_cleansed %}

#### Object Name
cmp_division_cleansed

#### Object Definition
Division(s) information of companies. User can set up division(s) in Division main panel under a specific company in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=cmp_division
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__cmp_division_versioned %}

#### Object Name
cmp_division_versioned

#### Object Definition
Division(s) information of companies. User can set up division(s) in Division main panel under a specific company in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=cmp_division
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}