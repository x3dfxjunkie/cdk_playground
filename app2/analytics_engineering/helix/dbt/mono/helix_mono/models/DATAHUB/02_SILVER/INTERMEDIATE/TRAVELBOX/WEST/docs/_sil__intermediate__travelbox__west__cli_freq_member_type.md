{% docs sil__intermediate__travelbox__west__cli_freq_member_type_cleansed %}

#### Object Name
cli_freq_member_type_cleansed

#### Object Definition
This table is used to store Frequent Client Membership Type information.
Frequent Client Membership Types are setup in Customer Profiles setup module, Setup menu

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=cli_freq_member_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__cli_freq_member_type_versioned %}

#### Object Name
cli_freq_member_type_versioned

#### Object Definition
This table is used to store Frequent Client Membership Type information.
Frequent Client Membership Types are setup in Customer Profiles setup module, Setup menu

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=cli_freq_member_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}