{% docs sil__intermediate__dreams__rooms_fulfillment__vip_lvl_cleansed %}

#### Object Name
vip_lvl_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_vip_lvl_nm & metadata_checksum combination.

#### Primary key
data_vip_lvl_nm

#### Tags
    - object_name=vip_lvl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__vip_lvl_versioned %}

#### Object Name
vip_lvl_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_vip_lvl_nm & metadata_checksum combination.

#### Primary key
data_vip_lvl_nm

#### Tags
    - object_name=vip_lvl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}