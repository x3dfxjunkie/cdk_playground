{% docs sil__intermediate__travelbox__west__res_flight_sector_cleansed %}

#### Object Name
res_flight_sector_cleansed

#### Object Definition
This contains all the sector level (itinerary level) information of the flight bookings in TravelBox

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_item_no, data_product_code, data_sector_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_item_no, data_product_code, data_sector_no

#### Tags
    - object_name=res_flight_sector
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__res_flight_sector_versioned %}

#### Object Name
res_flight_sector_versioned

#### Object Definition
This contains all the sector level (itinerary level) information of the flight bookings in TravelBox

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_item_no, data_product_code, data_sector_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_item_no, data_product_code, data_sector_no

#### Tags
    - object_name=res_flight_sector
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}