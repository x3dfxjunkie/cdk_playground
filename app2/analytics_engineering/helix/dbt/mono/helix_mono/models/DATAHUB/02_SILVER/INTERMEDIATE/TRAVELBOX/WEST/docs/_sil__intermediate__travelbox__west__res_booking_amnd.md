{% docs sil__intermediate__travelbox__west__res_booking_amnd_cleansed %}

#### Object Name
res_booking_amnd_cleansed

#### Object Definition
This table contains information of booking amendment charges.
These information are visible in Reservation Manager &gt; View Booking Amendment/Cancellation Charges panel.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_amnd_no, data_booking_id & metadata_checksum combination.

#### Primary key
data_amnd_no, data_booking_id

#### Tags
    - object_name=res_booking_amnd
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__res_booking_amnd_versioned %}

#### Object Name
res_booking_amnd_versioned

#### Object Definition
This table contains information of booking amendment charges.
These information are visible in Reservation Manager &gt; View Booking Amendment/Cancellation Charges panel.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_amnd_no, data_booking_id & metadata_checksum combination.

#### Primary key
data_amnd_no, data_booking_id

#### Tags
    - object_name=res_booking_amnd
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}