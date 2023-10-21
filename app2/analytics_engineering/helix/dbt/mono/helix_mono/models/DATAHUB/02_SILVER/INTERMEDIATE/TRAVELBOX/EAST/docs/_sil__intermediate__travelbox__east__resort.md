{% docs sil__intermediate__travelbox__east__resort_cleansed %}

#### Object Name
resort_cleansed

#### Object Definition
The tourist resorts defined for a particular city. Set up at &#39;Country/City/State/Resort&#39; under &#39;Destinations&#39; menu in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=resort
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__resort_versioned %}

#### Object Name
resort_versioned

#### Object Definition
The tourist resorts defined for a particular city. Set up at &#39;Country/City/State/Resort&#39; under &#39;Destinations&#39; menu in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=resort
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}