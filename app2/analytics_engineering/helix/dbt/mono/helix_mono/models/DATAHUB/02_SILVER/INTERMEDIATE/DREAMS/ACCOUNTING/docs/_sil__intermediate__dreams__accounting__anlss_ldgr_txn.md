{% docs sil__intermediate__dreams__accounting__anlss_ldgr_txn_cleansed %}

#### Object Name
anlss_ldgr_txn_cleansed

#### Object Definition
This table ties to the ALT Entry table for analysis purposes

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_anlss_ldgr_txn_id & metadata_checksum combination.

#### Primary key
data_anlss_ldgr_txn_id

#### Tags
    - object_name=anlss_ldgr_txn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__anlss_ldgr_txn_versioned %}

#### Object Name
anlss_ldgr_txn_versioned

#### Object Definition
This table ties to the ALT Entry table for analysis purposes

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_anlss_ldgr_txn_id & metadata_checksum combination.

#### Primary key
data_anlss_ldgr_txn_id

#### Tags
    - object_name=anlss_ldgr_txn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}