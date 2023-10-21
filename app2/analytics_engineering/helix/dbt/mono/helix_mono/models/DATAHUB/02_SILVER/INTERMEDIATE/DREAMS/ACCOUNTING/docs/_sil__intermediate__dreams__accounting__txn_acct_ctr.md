{% docs sil__intermediate__dreams__accounting__txn_acct_ctr_cleansed %}

#### Object Name
txn_acct_ctr_cleansed

#### Object Definition
Transaction Account Center IDs that are only Transaction Accounts

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_txn_acct_ctr_id & metadata_checksum combination.

#### Primary key
data_txn_acct_ctr_id

#### Tags
    - object_name=txn_acct_ctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__txn_acct_ctr_versioned %}

#### Object Name
txn_acct_ctr_versioned

#### Object Definition
Transaction Account Center IDs that are only Transaction Accounts

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_txn_acct_ctr_id & metadata_checksum combination.

#### Primary key
data_txn_acct_ctr_id

#### Tags
    - object_name=txn_acct_ctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}