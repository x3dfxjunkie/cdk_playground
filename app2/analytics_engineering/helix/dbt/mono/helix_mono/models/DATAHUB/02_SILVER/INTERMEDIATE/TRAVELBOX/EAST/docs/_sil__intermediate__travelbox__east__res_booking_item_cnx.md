{% docs sil__intermediate__travelbox__east__res_booking_item_cnx_cleansed %}

#### Object Name
res_booking_item_cnx_cleansed

#### Object Definition
This table holds the Cancellation information (cancalation cause  / reason, cancelation charges, etc) for all the cancelled booking items in TravelBox.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_index_no, data_item_no, data_product_code & metadata_checksum combination.

#### Primary key
data_booking_id, data_index_no, data_item_no, data_product_code

#### Tags
    - object_name=res_booking_item_cnx
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_booking_item_cnx_versioned %}

#### Object Name
res_booking_item_cnx_versioned

#### Object Definition
This table holds the Cancellation information (cancalation cause  / reason, cancelation charges, etc) for all the cancelled booking items in TravelBox.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_index_no, data_item_no, data_product_code & metadata_checksum combination.

#### Primary key
data_booking_id, data_index_no, data_item_no, data_product_code

#### Tags
    - object_name=res_booking_item_cnx
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}