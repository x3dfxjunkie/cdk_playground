{% docs sil__intermediate__travelbox__west__cli_marital_status_cleansed %}

#### Object Name
cli_marital_status_cleansed

#### Object Definition
This table is used to store Marital Statuses.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_marital_id & metadata_checksum combination.

#### Primary key
data_marital_id

#### Tags
    - object_name=cli_marital_status
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__cli_marital_status_versioned %}

#### Object Name
cli_marital_status_versioned

#### Object Definition
This table is used to store Marital Statuses.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_marital_id & metadata_checksum combination.

#### Primary key
data_marital_id

#### Tags
    - object_name=cli_marital_status
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}