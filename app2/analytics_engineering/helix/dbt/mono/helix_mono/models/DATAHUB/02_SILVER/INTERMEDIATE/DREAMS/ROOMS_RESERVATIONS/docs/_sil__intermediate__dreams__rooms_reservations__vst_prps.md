{% docs sil__intermediate__dreams__rooms_reservations__vst_prps_cleansed %}

#### Object Name
vst_prps_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_vst_prps_nm & metadata_checksum combination.

#### Primary key
data_vst_prps_nm

#### Tags
    - object_name=vst_prps
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__vst_prps_versioned %}

#### Object Name
vst_prps_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_vst_prps_nm & metadata_checksum combination.

#### Primary key
data_vst_prps_nm

#### Tags
    - object_name=vst_prps
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}