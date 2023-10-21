{% docs sil__intermediate__travelbox__east__act_client_cc_receipt_cleansed %}

#### Object Name
act_client_cc_receipt_cleansed

#### Object Definition
This table is used to store information of payments done using Credit Card as the payment Type.
The values are setup in adding Receipts by selecting the Credit Card as the payment type.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_receipt_index & metadata_checksum combination.

#### Primary key
data_booking_id, data_receipt_index

#### Tags
    - object_name=act_client_cc_receipt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__act_client_cc_receipt_versioned %}

#### Object Name
act_client_cc_receipt_versioned

#### Object Definition
This table is used to store information of payments done using Credit Card as the payment Type.
The values are setup in adding Receipts by selecting the Credit Card as the payment type.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_receipt_index & metadata_checksum combination.

#### Primary key
data_booking_id, data_receipt_index

#### Tags
    - object_name=act_client_cc_receipt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}