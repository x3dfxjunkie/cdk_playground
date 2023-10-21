{% docs sil__intermediate__travelbox__west__city_cleansed %}

#### Object Name
city_cleansed

#### Object Definition
This table contains user defined city information for a specific region and a country. Set up at Country/City/State/Resort panel in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=city
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__city_versioned %}

#### Object Name
city_versioned

#### Object Definition
This table contains user defined city information for a specific region and a country. Set up at Country/City/State/Resort panel in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=city
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}