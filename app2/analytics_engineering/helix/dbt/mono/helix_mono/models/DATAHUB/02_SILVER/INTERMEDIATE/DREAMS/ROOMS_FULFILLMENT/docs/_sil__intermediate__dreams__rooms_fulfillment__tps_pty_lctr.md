{% docs sil__intermediate__dreams__rooms_fulfillment__tps_pty_lctr_cleansed %}

#### Object Name
tps_pty_lctr_cleansed

#### Object Definition
This table ties the guest/travel agency on a reservation to a locator type by last name, first name and transactional party ID., Address, Email, Phone

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tps_id & metadata_checksum combination.

#### Primary key
data_tps_id

#### Tags
    - object_name=tps_pty_lctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__tps_pty_lctr_versioned %}

#### Object Name
tps_pty_lctr_versioned

#### Object Definition
This table ties the guest/travel agency on a reservation to a locator type by last name, first name and transactional party ID., Address, Email, Phone

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tps_id & metadata_checksum combination.

#### Primary key
data_tps_id

#### Tags
    - object_name=tps_pty_lctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}