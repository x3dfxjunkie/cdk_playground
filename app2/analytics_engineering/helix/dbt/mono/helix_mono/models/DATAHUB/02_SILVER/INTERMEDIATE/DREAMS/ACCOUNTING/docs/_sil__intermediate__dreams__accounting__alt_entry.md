{% docs sil__intermediate__dreams__accounting__alt_entry_cleansed %}

#### Object Name
alt_entry_cleansed

#### Object Definition
Provides a means of distributing transaction values to ledger accounts together with analysis information, this table represents the record-keeping system for a company&#39;s ficial data, with debit and credit account records validated by a trial balance.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_anlss_ldgr_txn_entry_id & metadata_checksum combination.

#### Primary key
data_anlss_ldgr_txn_entry_id

#### Tags
    - object_name=alt_entry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__alt_entry_versioned %}

#### Object Name
alt_entry_versioned

#### Object Definition
Provides a means of distributing transaction values to ledger accounts together with analysis information, this table represents the record-keeping system for a company&#39;s ficial data, with debit and credit account records validated by a trial balance.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_anlss_ldgr_txn_entry_id & metadata_checksum combination.

#### Primary key
data_anlss_ldgr_txn_entry_id

#### Tags
    - object_name=alt_entry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}