{% docs sil__intermediate__dreams__guest__txn_idvl_pty_mbshp_cleansed %}

#### Object Name
txn_idvl_pty_mbshp_cleansed

#### Object Definition
Membership IDs associated to transactional individual IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_txn_idvl_pty_mbrshp_id & metadata_checksum combination.

#### Primary key
data_txn_idvl_pty_mbrshp_id

#### Tags
    - object_name=txn_idvl_pty_mbshp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest__txn_idvl_pty_mbshp_versioned %}

#### Object Name
txn_idvl_pty_mbshp_versioned

#### Object Definition
Membership IDs associated to transactional individual IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_txn_idvl_pty_mbrshp_id & metadata_checksum combination.

#### Primary key
data_txn_idvl_pty_mbrshp_id

#### Tags
    - object_name=txn_idvl_pty_mbshp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}