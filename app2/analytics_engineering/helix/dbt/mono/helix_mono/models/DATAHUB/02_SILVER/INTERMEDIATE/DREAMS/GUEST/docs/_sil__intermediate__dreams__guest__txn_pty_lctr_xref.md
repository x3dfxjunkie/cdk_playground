{% docs sil__intermediate__dreams__guest__txn_pty_lctr_xref_cleansed %}

#### Object Name
txn_pty_lctr_xref_cleansed

#### Object Definition
This table provides a reference to locator IDs in GOMaster

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_txn_pty_lctr_extnl_ref_id & metadata_checksum combination.

#### Primary key
data_txn_pty_lctr_extnl_ref_id

#### Tags
    - object_name=txn_pty_lctr_xref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest__txn_pty_lctr_xref_versioned %}

#### Object Name
txn_pty_lctr_xref_versioned

#### Object Definition
This table provides a reference to locator IDs in GOMaster

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_txn_pty_lctr_extnl_ref_id & metadata_checksum combination.

#### Primary key
data_txn_pty_lctr_extnl_ref_id

#### Tags
    - object_name=txn_pty_lctr_xref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}