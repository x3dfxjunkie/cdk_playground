{% docs sil__intermediate__dreams__accounting__rfnd_ap_cleansed %}

#### Object Name
rfnd_ap_cleansed

#### Object Definition
Accounts Payable Refund Transactions with SAP and Accounting Center information

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_ap_id & metadata_checksum combination.

#### Primary key
data_ap_id

#### Tags
    - object_name=rfnd_ap
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__rfnd_ap_versioned %}

#### Object Name
rfnd_ap_versioned

#### Object Definition
Accounts Payable Refund Transactions with SAP and Accounting Center information

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_ap_id & metadata_checksum combination.

#### Primary key
data_ap_id

#### Tags
    - object_name=rfnd_ap
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}