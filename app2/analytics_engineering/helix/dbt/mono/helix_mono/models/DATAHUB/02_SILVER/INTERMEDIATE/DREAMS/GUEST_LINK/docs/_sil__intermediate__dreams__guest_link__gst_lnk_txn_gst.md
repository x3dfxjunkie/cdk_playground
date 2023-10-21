{% docs sil__intermediate__dreams__guest_link__gst_lnk_txn_gst_cleansed %}

#### Object Name
gst_lnk_txn_gst_cleansed

#### Object Definition
This table associates the guest link ID to the Guest Link Transaction Guest ID and the Transaction Guest ID and the inactive datetime would be populated if the record is inactive

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_gst_lnk_txn_gst_id & metadata_checksum combination.

#### Primary key
data_gst_lnk_txn_gst_id

#### Tags
    - object_name=gst_lnk_txn_gst
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest_link__gst_lnk_txn_gst_versioned %}

#### Object Name
gst_lnk_txn_gst_versioned

#### Object Definition
This table associates the guest link ID to the Guest Link Transaction Guest ID and the Transaction Guest ID and the inactive datetime would be populated if the record is inactive

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_gst_lnk_txn_gst_id & metadata_checksum combination.

#### Primary key
data_gst_lnk_txn_gst_id

#### Tags
    - object_name=gst_lnk_txn_gst
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}