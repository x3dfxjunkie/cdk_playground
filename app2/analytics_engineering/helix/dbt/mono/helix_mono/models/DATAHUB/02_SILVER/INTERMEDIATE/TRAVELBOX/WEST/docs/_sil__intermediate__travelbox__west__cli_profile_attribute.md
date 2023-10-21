{% docs sil__intermediate__travelbox__west__cli_profile_attribute_cleansed %}

#### Object Name
cli_profile_attribute_cleansed

#### Object Definition
This table is used to store passenger attribute values with respect to each Passenger Profiles.
Passenger profile attribute values are entered in Attributes panel of the Direct Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_attribute_id, data_profile_id & metadata_checksum combination.

#### Primary key
data_attribute_id, data_profile_id

#### Tags
    - object_name=cli_profile_attribute
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__cli_profile_attribute_versioned %}

#### Object Name
cli_profile_attribute_versioned

#### Object Definition
This table is used to store passenger attribute values with respect to each Passenger Profiles.
Passenger profile attribute values are entered in Attributes panel of the Direct Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_attribute_id, data_profile_id & metadata_checksum combination.

#### Primary key
data_attribute_id, data_profile_id

#### Tags
    - object_name=cli_profile_attribute
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}