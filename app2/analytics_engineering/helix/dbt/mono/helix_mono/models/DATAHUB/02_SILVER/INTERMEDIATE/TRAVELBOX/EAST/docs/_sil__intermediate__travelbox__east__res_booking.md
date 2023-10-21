{% docs sil__intermediate__travelbox__east__res_booking_cleansed %}

#### Object Name
res_booking_cleansed

#### Object Definition
This table stores all the to level information related to all the bookings or Quotations made in TravelBox Reservation system.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id & metadata_checksum combination.

#### Primary key
data_booking_id

#### Tags
    - object_name=res_booking
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_booking_versioned %}

#### Object Name
res_booking_versioned

#### Object Definition
This table stores all the to level information related to all the bookings or Quotations made in TravelBox Reservation system.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id & metadata_checksum combination.

#### Primary key
data_booking_id

#### Tags
    - object_name=res_booking
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}