{% docs sil__intermediate__dreams__dining__tps_lctr_cleansed %}

#### Object Name
tps_lctr_cleansed

#### Object Definition
This table contains locator IDs associated to the reservation by locator type:(MobilePush, Email, Phone)

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tps_id, data_tps_lctr_id & metadata_checksum combination.

#### Primary key
data_tps_id, data_tps_lctr_id

#### Tags
    - object_name=tps_lctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__tps_lctr_versioned %}

#### Object Name
tps_lctr_versioned

#### Object Definition
This table contains locator IDs associated to the reservation by locator type:(MobilePush, Email, Phone)

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tps_id, data_tps_lctr_id & metadata_checksum combination.

#### Primary key
data_tps_id, data_tps_lctr_id

#### Tags
    - object_name=tps_lctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}