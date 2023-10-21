{% docs sil__intermediate__travelbox__east__res_generic_discount_cleansed %}

#### Object Name
res_generic_discount_cleansed

#### Object Definition
This stores information related to booking item Discounts which are offered at the Generic contract level.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_discount_no, data_item_no, data_product_code & metadata_checksum combination.

#### Primary key
data_booking_id, data_discount_no, data_item_no, data_product_code

#### Tags
    - object_name=res_generic_discount
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_generic_discount_versioned %}

#### Object Name
res_generic_discount_versioned

#### Object Definition
This stores information related to booking item Discounts which are offered at the Generic contract level.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_discount_no, data_item_no, data_product_code & metadata_checksum combination.

#### Primary key
data_booking_id, data_discount_no, data_item_no, data_product_code

#### Tags
    - object_name=res_generic_discount
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}