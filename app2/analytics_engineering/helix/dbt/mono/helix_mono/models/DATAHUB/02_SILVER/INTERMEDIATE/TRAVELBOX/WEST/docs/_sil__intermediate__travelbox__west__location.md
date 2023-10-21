{% docs sil__intermediate__travelbox__west__location_cleansed %}

#### Object Name
location_cleansed

#### Object Definition
Pick up and Drop off locations for transfers. Set up data under &#39;Locations&#39; menu item in &#39;Destinations&#39; menu of Setup Client and &#39;Setup&#39; menu in Transfer Loading Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_location_id & metadata_checksum combination.

#### Primary key
data_location_id

#### Tags
    - object_name=location
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__location_versioned %}

#### Object Name
location_versioned

#### Object Definition
Pick up and Drop off locations for transfers. Set up data under &#39;Locations&#39; menu item in &#39;Destinations&#39; menu of Setup Client and &#39;Setup&#39; menu in Transfer Loading Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_location_id & metadata_checksum combination.

#### Primary key
data_location_id

#### Tags
    - object_name=location
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}