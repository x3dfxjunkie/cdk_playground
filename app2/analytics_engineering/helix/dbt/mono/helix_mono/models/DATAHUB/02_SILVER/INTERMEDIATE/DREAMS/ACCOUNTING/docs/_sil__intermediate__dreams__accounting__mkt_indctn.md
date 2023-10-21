{% docs sil__intermediate__dreams__accounting__mkt_indctn_cleansed %}

#### Object Name
mkt_indctn_cleansed

#### Object Definition
One record with a code for Resort Reservations

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_mkt_indctn_cd & metadata_checksum combination.

#### Primary key
data_mkt_indctn_cd

#### Tags
    - object_name=mkt_indctn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__mkt_indctn_versioned %}

#### Object Name
mkt_indctn_versioned

#### Object Definition
One record with a code for Resort Reservations

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_mkt_indctn_cd & metadata_checksum combination.

#### Primary key
data_mkt_indctn_cd

#### Tags
    - object_name=mkt_indctn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}