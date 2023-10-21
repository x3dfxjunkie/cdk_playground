{% docs sil__intermediate__travelbox__west__brand_cleansed %}

#### Object Name
brand_cleansed

#### Object Definition
Contains user defined code name mapping of brands, set up at Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=brand
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__brand_versioned %}

#### Object Name
brand_versioned

#### Object Definition
Contains user defined code name mapping of brands, set up at Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=brand
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}