{% docs sil__intermediate__dreams__accounting__bank_acct_ctr_cleansed %}

#### Object Name
bank_acct_ctr_cleansed

#### Object Definition
This holds information about the Accounting Centers where payments are taken

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_bank_acct_ctr_id & metadata_checksum combination.

#### Primary key
data_bank_acct_ctr_id

#### Tags
    - object_name=bank_acct_ctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__bank_acct_ctr_versioned %}

#### Object Name
bank_acct_ctr_versioned

#### Object Definition
This holds information about the Accounting Centers where payments are taken

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_bank_acct_ctr_id & metadata_checksum combination.

#### Primary key
data_bank_acct_ctr_id

#### Tags
    - object_name=bank_acct_ctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}