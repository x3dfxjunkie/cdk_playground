{% docs sil__intermediate__travelbox__east__res_booking_fee_cleansed %}

#### Object Name
res_booking_fee_cleansed

#### Object Definition
This table holds the information related to Fees applicable for bookings. Booking Fees can be applied manualy or automatically from Reservation module

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_fee_code, data_fee_code_index & metadata_checksum combination.

#### Primary key
data_booking_id, data_fee_code, data_fee_code_index

#### Tags
    - object_name=res_booking_fee
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_booking_fee_versioned %}

#### Object Name
res_booking_fee_versioned

#### Object Definition
This table holds the information related to Fees applicable for bookings. Booking Fees can be applied manualy or automatically from Reservation module

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_fee_code, data_fee_code_index & metadata_checksum combination.

#### Primary key
data_booking_id, data_fee_code, data_fee_code_index

#### Tags
    - object_name=res_booking_fee
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}