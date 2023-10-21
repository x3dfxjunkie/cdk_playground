{% docs sil__intermediate__travelbox__east__res_booking_package_cleansed %}

#### Object Name
res_booking_package_cleansed

#### Object Definition
This contains booking package level information of all the bookings.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_package_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_package_no

#### Tags
    - object_name=res_booking_package
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_booking_package_versioned %}

#### Object Name
res_booking_package_versioned

#### Object Definition
This contains booking package level information of all the bookings.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_package_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_package_no

#### Tags
    - object_name=res_booking_package
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}