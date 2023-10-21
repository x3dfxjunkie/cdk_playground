{% docs sil__intermediate__travelbox__west__res_booking_type_cleansed %}

#### Object Name
res_booking_type_cleansed

#### Object Definition
This table holds the Travelbox booking types specific to the environment. Examples possible values are Group, Standard, Lockbox, Refund.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=res_booking_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__res_booking_type_versioned %}

#### Object Name
res_booking_type_versioned

#### Object Definition
This table holds the Travelbox booking types specific to the environment. Examples possible values are Group, Standard, Lockbox, Refund.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=res_booking_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}