{% docs sil__intermediate__dreams__folio__folio_txn_bal_cleansed %}

#### Object Name
folio_txn_bal_cleansed

#### Object Definition
This table ties a Folio ID to a Folio Transaction ID and the Folio Balance Amount

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_folio_id, data_folio_txn_id & metadata_checksum combination.

#### Primary key
data_folio_id, data_folio_txn_id

#### Tags
    - object_name=folio_txn_bal
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__folio_txn_bal_versioned %}

#### Object Name
folio_txn_bal_versioned

#### Object Definition
This table ties a Folio ID to a Folio Transaction ID and the Folio Balance Amount

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_folio_id, data_folio_txn_id & metadata_checksum combination.

#### Primary key
data_folio_id, data_folio_txn_id

#### Tags
    - object_name=folio_txn_bal
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}