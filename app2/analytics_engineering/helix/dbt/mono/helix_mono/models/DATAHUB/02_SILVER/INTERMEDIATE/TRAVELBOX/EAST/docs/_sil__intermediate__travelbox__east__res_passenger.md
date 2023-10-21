{% docs sil__intermediate__travelbox__east__res_passenger_cleansed %}

#### Object Name
res_passenger_cleansed

#### Object Definition
This is the main table maintaining the mapping between the passenger profile and the booking.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_passenger_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_passenger_no

#### Tags
    - object_name=res_passenger
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_passenger_versioned %}

#### Object Name
res_passenger_versioned

#### Object Definition
This is the main table maintaining the mapping between the passenger profile and the booking.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_passenger_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_passenger_no

#### Tags
    - object_name=res_passenger
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}