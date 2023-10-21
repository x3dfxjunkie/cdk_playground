{% docs sil__intermediate__dreams__folio__trvl_agcy_cleansed %}

#### Object Name
trvl_agcy_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_trvl_agcy_id & metadata_checksum combination.

#### Primary key
data_trvl_agcy_id

#### Tags
    - object_name=trvl_agcy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__trvl_agcy_versioned %}

#### Object Name
trvl_agcy_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_trvl_agcy_id & metadata_checksum combination.

#### Primary key
data_trvl_agcy_id

#### Tags
    - object_name=trvl_agcy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}