{% docs sil__intermediate__travelbox__east__res_bkg_usr_defined_type_cleansed %}

#### Object Name
res_bkg_usr_defined_type_cleansed

#### Object Definition
User defined types related to reservation bookings

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_attribute_id, data_booking_id, data_index_no & metadata_checksum combination.

#### Primary key
data_attribute_id, data_booking_id, data_index_no

#### Tags
    - object_name=res_bkg_usr_defined_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__res_bkg_usr_defined_type_versioned %}

#### Object Name
res_bkg_usr_defined_type_versioned

#### Object Definition
User defined types related to reservation bookings

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_attribute_id, data_booking_id, data_index_no & metadata_checksum combination.

#### Primary key
data_attribute_id, data_booking_id, data_index_no

#### Tags
    - object_name=res_bkg_usr_defined_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}