{% docs sil__intermediate__travelbox__west__res_booking_item_cleansed %}

#### Object Name
res_booking_item_cleansed

#### Object Definition
This contains all the basic information of Booking Product Items common to all product types.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_item_no, data_product_code & metadata_checksum combination.

#### Primary key
data_booking_id, data_item_no, data_product_code

#### Tags
    - object_name=res_booking_item
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__res_booking_item_versioned %}

#### Object Name
res_booking_item_versioned

#### Object Definition
This contains all the basic information of Booking Product Items common to all product types.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_item_no, data_product_code & metadata_checksum combination.

#### Primary key
data_booking_id, data_item_no, data_product_code

#### Tags
    - object_name=res_booking_item
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}