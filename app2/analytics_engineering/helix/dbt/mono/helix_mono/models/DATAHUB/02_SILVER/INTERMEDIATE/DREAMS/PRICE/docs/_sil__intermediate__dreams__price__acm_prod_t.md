{% docs sil__intermediate__dreams__price__acm_prod_t_cleansed %}

#### Object Name
acm_prod_t_cleansed

#### Object Definition
This provides the Accommodation (hotel room, villa, campsite) room type code as well as the threshold for that room when the Accommodation is a double occupancy, the extra guests pay an additional charge per night

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acm_prod_id & metadata_checksum combination.

#### Primary key
data_acm_prod_id

#### Tags
    - object_name=acm_prod_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__acm_prod_t_versioned %}

#### Object Name
acm_prod_t_versioned

#### Object Definition
This provides the Accommodation (hotel room, villa, campsite) room type code as well as the threshold for that room when the Accommodation is a double occupancy, the extra guests pay an additional charge per night

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acm_prod_id & metadata_checksum combination.

#### Primary key
data_acm_prod_id

#### Tags
    - object_name=acm_prod_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}