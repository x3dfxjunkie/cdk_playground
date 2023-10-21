{% docs sil__intermediate__dreams__guest__txn_pty_cleansed %}

#### Object Name
txn_pty_cleansed

#### Object Definition
This table contains both Organization Transactional Party ID and Transactional Individual Party ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_txn_pty_id & metadata_checksum combination.

#### Primary key
data_txn_pty_id

#### Tags
    - object_name=txn_pty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest__txn_pty_versioned %}

#### Object Name
txn_pty_versioned

#### Object Definition
This table contains both Organization Transactional Party ID and Transactional Individual Party ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_txn_pty_id & metadata_checksum combination.

#### Primary key
data_txn_pty_id

#### Tags
    - object_name=txn_pty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}