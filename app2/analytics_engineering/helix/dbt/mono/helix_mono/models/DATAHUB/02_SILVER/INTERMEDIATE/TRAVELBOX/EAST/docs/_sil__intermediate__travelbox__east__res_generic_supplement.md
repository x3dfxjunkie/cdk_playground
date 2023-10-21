{% docs sil__intermediate__travelbox__east__res_generic_supplement_cleansed %}

#### Object Name
res_generic_supplement_cleansed

#### Object Definition
This holds information related to the Supplementory items booked with Generic itemes. These Supplements are offered / defined at the Generic contract.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_item_no, data_product_code, data_supplement_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_item_no, data_product_code, data_supplement_no

#### Tags
    - object_name=res_generic_supplement
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_generic_supplement_versioned %}

#### Object Name
res_generic_supplement_versioned

#### Object Definition
This holds information related to the Supplementory items booked with Generic itemes. These Supplements are offered / defined at the Generic contract.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_item_no, data_product_code, data_supplement_no & metadata_checksum combination.

#### Primary key
data_booking_id, data_item_no, data_product_code, data_supplement_no

#### Tags
    - object_name=res_generic_supplement
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}