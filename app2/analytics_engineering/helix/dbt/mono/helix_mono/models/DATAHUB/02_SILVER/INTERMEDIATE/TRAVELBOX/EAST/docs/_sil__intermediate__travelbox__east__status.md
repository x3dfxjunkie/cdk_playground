{% docs sil__intermediate__travelbox__east__status_cleansed %}

#### Object Name
status_cleansed

#### Object Definition
The different statuses a contract can have in TravelBox. Set up under &#39;Contracting&#39; menu in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_status_id & metadata_checksum combination.

#### Primary key
data_status_id

#### Tags
    - object_name=status
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__status_versioned %}

#### Object Name
status_versioned

#### Object Definition
The different statuses a contract can have in TravelBox. Set up under &#39;Contracting&#39; menu in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_status_id & metadata_checksum combination.

#### Primary key
data_status_id

#### Tags
    - object_name=status
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}