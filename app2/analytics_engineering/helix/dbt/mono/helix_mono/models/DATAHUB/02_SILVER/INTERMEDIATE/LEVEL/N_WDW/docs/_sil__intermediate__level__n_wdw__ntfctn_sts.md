{% docs sil__intermediate__level__n_wdw__ntfctn_sts_cleansed %}

#### Object Name
ntfctn_sts_cleansed

#### Object Definition
Reference table containing notification status. such as IN_PROGRESS, SUCCESS, FAILED, AND TIMEOUT.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_ntfctn_sts_id & metadata_checksum combination.

#### Primary key
data_ntfctn_sts_id

#### Tags
    - object_name=ntfctn_sts
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__ntfctn_sts_versioned %}

#### Object Name
ntfctn_sts_versioned

#### Object Definition
Reference table containing notification status. such as IN_PROGRESS, SUCCESS, FAILED, AND TIMEOUT.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_ntfctn_sts_id & metadata_checksum combination.

#### Primary key
data_ntfctn_sts_id

#### Tags
    - object_name=ntfctn_sts
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}