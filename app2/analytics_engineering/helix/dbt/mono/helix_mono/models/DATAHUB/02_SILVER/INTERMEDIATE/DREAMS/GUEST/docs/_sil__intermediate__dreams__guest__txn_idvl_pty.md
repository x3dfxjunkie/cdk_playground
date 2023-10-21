{% docs sil__intermediate__dreams__guest__txn_idvl_pty_cleansed %}

#### Object Name
txn_idvl_pty_cleansed

#### Object Definition
Provides a transactional ID associated with an individual guest

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_txn_idvl_pty_id & metadata_checksum combination.

#### Primary key
data_txn_idvl_pty_id

#### Tags
    - object_name=txn_idvl_pty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest__txn_idvl_pty_versioned %}

#### Object Name
txn_idvl_pty_versioned

#### Object Definition
Provides a transactional ID associated with an individual guest

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_txn_idvl_pty_id & metadata_checksum combination.

#### Primary key
data_txn_idvl_pty_id

#### Tags
    - object_name=txn_idvl_pty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}