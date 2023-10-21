{% docs sil__intermediate__travelbox__west__state_cleansed %}

#### Object Name
state_cleansed

#### Object Definition
Travelbox geographical &#39;State&#39; for a particular country. Set up at &#39;Country/City/State/Resort&#39; under &#39;Destinations&#39; manu in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=state
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__state_versioned %}

#### Object Name
state_versioned

#### Object Definition
Travelbox geographical &#39;State&#39; for a particular country. Set up at &#39;Country/City/State/Resort&#39; under &#39;Destinations&#39; manu in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=state
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}