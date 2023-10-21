{% docs sil__intermediate__travelbox__west__res_option_status_cleansed %}

#### Object Name
res_option_status_cleansed

#### Object Definition
Status defining the state of a reservation and payment

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=res_option_status
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__res_option_status_versioned %}

#### Object Name
res_option_status_versioned

#### Object Definition
Status defining the state of a reservation and payment

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=res_option_status
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}