{% docs sil__intermediate__dreams__guest_link__txn_gst_xref_cleansed %}

#### Object Name
txn_gst_xref_cleansed

#### Object Definition
This table links the Transaction Guest Crossreference source name: CHARGE_ACCOUNT_ID to the Guest Link Transaction Guest ID to provide the Transaction Guest Crossreference value

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_gst_lnk_txn_gst_id & metadata_checksum combination.

#### Primary key
data_gst_lnk_txn_gst_id

#### Tags
    - object_name=txn_gst_xref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest_link__txn_gst_xref_versioned %}

#### Object Name
txn_gst_xref_versioned

#### Object Definition
This table links the Transaction Guest Crossreference source name: CHARGE_ACCOUNT_ID to the Guest Link Transaction Guest ID to provide the Transaction Guest Crossreference value

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_gst_lnk_txn_gst_id & metadata_checksum combination.

#### Primary key
data_gst_lnk_txn_gst_id

#### Tags
    - object_name=txn_gst_xref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}