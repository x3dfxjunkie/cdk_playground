{% docs sil__intermediate__travelbox__west__cli_direct_client_cleansed %}

#### Object Name
cli_direct_client_cleansed

#### Object Definition
This table is used to store information associated with a Direct Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_client_id & metadata_checksum combination.

#### Primary key
data_client_id

#### Tags
    - object_name=cli_direct_client
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__cli_direct_client_versioned %}

#### Object Name
cli_direct_client_versioned

#### Object Definition
This table is used to store information associated with a Direct Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_client_id & metadata_checksum combination.

#### Primary key
data_client_id

#### Tags
    - object_name=cli_direct_client
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}