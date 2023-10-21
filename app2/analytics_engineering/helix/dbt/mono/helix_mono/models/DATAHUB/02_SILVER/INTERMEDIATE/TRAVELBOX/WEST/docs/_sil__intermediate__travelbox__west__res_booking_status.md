{% docs sil__intermediate__travelbox__west__res_booking_status_cleansed %}

#### Object Name
res_booking_status_cleansed

#### Object Definition
This contains system defined master data of TravelBox Booking statuses.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=res_booking_status
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__res_booking_status_versioned %}

#### Object Name
res_booking_status_versioned

#### Object Definition
This contains system defined master data of TravelBox Booking statuses.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=res_booking_status
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}