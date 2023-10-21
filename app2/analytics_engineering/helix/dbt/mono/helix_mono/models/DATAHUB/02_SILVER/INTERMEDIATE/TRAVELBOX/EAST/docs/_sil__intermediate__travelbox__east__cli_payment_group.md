{% docs sil__intermediate__travelbox__east__cli_payment_group_cleansed %}

#### Object Name
cli_payment_group_cleansed

#### Object Definition
This table is used to keep Payment Group stored.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=cli_payment_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__cli_payment_group_versioned %}

#### Object Name
cli_payment_group_versioned

#### Object Definition
This table is used to keep Payment Group stored.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=cli_payment_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}