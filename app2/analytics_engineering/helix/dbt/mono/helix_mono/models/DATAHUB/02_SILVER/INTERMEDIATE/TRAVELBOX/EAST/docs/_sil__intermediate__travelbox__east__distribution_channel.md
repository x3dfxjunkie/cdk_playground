{% docs sil__intermediate__travelbox__east__distribution_channel_cleansed %}

#### Object Name
distribution_channel_cleansed

#### Object Definition
The distribution channels used within TravelBox. Set up at setup menu in Markup Manager

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=distribution_channel
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__distribution_channel_versioned %}

#### Object Name
distribution_channel_versioned

#### Object Definition
The distribution channels used within TravelBox. Set up at setup menu in Markup Manager

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=distribution_channel
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}