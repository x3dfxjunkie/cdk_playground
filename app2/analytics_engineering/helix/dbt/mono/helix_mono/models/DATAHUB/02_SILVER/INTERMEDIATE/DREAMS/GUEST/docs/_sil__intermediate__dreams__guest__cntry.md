{% docs sil__intermediate__dreams__guest__cntry_cleansed %}

#### Object Name
cntry_cleansed

#### Object Definition
Country Codes and Names

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cntry_cd & metadata_checksum combination.

#### Primary key
data_cntry_cd

#### Tags
    - object_name=cntry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest__cntry_versioned %}

#### Object Name
cntry_versioned

#### Object Definition
Country Codes and Names

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cntry_cd & metadata_checksum combination.

#### Primary key
data_cntry_cd

#### Tags
    - object_name=cntry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}