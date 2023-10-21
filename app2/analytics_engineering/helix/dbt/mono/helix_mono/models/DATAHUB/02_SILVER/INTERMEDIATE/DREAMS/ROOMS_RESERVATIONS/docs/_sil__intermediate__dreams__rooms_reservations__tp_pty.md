{% docs sil__intermediate__dreams__rooms_reservations__tp_pty_cleansed %}

#### Object Name
tp_pty_cleansed

#### Object Definition
This table provides all the guest IDs associated to their Travel Plan

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tp_id, data_txn_pty_id & metadata_checksum combination.

#### Primary key
data_tp_id, data_txn_pty_id

#### Tags
    - object_name=tp_pty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tp_pty_versioned %}

#### Object Name
tp_pty_versioned

#### Object Definition
This table provides all the guest IDs associated to their Travel Plan

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tp_id, data_txn_pty_id & metadata_checksum combination.

#### Primary key
data_tp_id, data_txn_pty_id

#### Tags
    - object_name=tp_pty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}