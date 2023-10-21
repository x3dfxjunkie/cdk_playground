{% docs sil__intermediate__das__wdw__lnk_assc_cleansed %}

#### Object Name
lnk_assc_cleansed

#### Object Definition
Table to track when links are merged in DAS.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_actv_lnk_id, data_mergd_lnk_id & metadata_checksum combination.

#### Primary key
data_actv_lnk_id, data_mergd_lnk_id

#### Tags
    - object_name=lnk_assc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__das__wdw__lnk_assc_versioned %}

#### Object Name
lnk_assc_versioned

#### Object Definition
Table to track when links are merged in DAS.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_actv_lnk_id, data_mergd_lnk_id & metadata_checksum combination.

#### Primary key
data_actv_lnk_id, data_mergd_lnk_id

#### Tags
    - object_name=lnk_assc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}