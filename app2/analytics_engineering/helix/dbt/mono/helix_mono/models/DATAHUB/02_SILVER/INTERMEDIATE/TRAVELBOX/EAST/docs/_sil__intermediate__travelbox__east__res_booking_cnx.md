{% docs sil__intermediate__travelbox__east__res_booking_cnx_cleansed %}

#### Object Name
res_booking_cnx_cleansed

#### Object Definition
This table holds the Cancellation information (cancalation cause  / reason, cancelation charges, etc) for all the cancelled bookings in TravelBox.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_cnx_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_cnx_no

#### Tags
    - object_name=res_booking_cnx
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_booking_cnx_versioned %}

#### Object Name
res_booking_cnx_versioned

#### Object Definition
This table holds the Cancellation information (cancalation cause  / reason, cancelation charges, etc) for all the cancelled bookings in TravelBox.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_cnx_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_cnx_no

#### Tags
    - object_name=res_booking_cnx
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}