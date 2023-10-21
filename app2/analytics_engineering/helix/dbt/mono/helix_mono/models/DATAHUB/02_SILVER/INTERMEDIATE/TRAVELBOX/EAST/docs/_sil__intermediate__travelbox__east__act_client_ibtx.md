{% docs sil__intermediate__travelbox__east__act_client_ibtx_cleansed %}

#### Object Name
act_client_ibtx_cleansed

#### Object Definition
This table is used to store information of IBTX payments. The values are setup in &#39;Search Receipts-&gt;
IBTX&#39; in Accounts Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_receipt_index & metadata_checksum combination.

#### Primary key
data_booking_id, data_receipt_index

#### Tags
    - object_name=act_client_ibtx
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__act_client_ibtx_versioned %}

#### Object Name
act_client_ibtx_versioned

#### Object Definition
This table is used to store information of IBTX payments. The values are setup in &#39;Search Receipts-&gt;
IBTX&#39; in Accounts Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_receipt_index & metadata_checksum combination.

#### Primary key
data_booking_id, data_receipt_index

#### Tags
    - object_name=act_client_ibtx
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}