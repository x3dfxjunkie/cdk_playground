{% docs sil__intermediate__dreams__folio__txn_rsn_cleansed %}

#### Object Name
txn_rsn_cleansed

#### Object Definition
This table associates a transaction reason type and transaction reason name to a transaction reason code

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_txn_rsn_cd & metadata_checksum combination.

#### Primary key
data_txn_rsn_cd

#### Tags
    - object_name=txn_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__txn_rsn_versioned %}

#### Object Name
txn_rsn_versioned

#### Object Definition
This table associates a transaction reason type and transaction reason name to a transaction reason code

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_txn_rsn_cd & metadata_checksum combination.

#### Primary key
data_txn_rsn_cd

#### Tags
    - object_name=txn_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}