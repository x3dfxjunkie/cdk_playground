{% docs sil__intermediate__dreams__guest__rgn_cleansed %}

#### Object Name
rgn_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cntry_cd, data_rgn_cd & metadata_checksum combination.

#### Primary key
data_cntry_cd, data_rgn_cd

#### Tags
    - object_name=rgn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest__rgn_versioned %}

#### Object Name
rgn_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cntry_cd, data_rgn_cd & metadata_checksum combination.

#### Primary key
data_cntry_cd, data_rgn_cd

#### Tags
    - object_name=rgn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}