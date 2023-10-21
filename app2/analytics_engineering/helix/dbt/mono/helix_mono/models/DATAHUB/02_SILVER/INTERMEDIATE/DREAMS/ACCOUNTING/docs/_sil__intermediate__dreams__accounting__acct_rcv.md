{% docs sil__intermediate__dreams__accounting__acct_rcv_cleansed %}

#### Object Name
acct_rcv_cleansed

#### Object Definition
Account Receivable information from SAP and Accounting, ie: PMT_ID, CAMPUS and the Business Organization ID, etc

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acct_rcv_id & metadata_checksum combination.

#### Primary key
data_acct_rcv_id

#### Tags
    - object_name=acct_rcv
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__acct_rcv_versioned %}

#### Object Name
acct_rcv_versioned

#### Object Definition
Account Receivable information from SAP and Accounting, ie: PMT_ID, CAMPUS and the Business Organization ID, etc

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acct_rcv_id & metadata_checksum combination.

#### Primary key
data_acct_rcv_id

#### Tags
    - object_name=acct_rcv
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}