{% docs sil__intermediate__dreams__accounting__acct_ctr_pst_acct_cleansed %}

#### Object Name
acct_ctr_pst_acct_cleansed

#### Object Definition
This table contains the association of the post account start and end dates for the account center and charge account center

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acct_ctr_pst_acct_id & metadata_checksum combination.

#### Primary key
data_acct_ctr_pst_acct_id

#### Tags
    - object_name=acct_ctr_pst_acct
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__acct_ctr_pst_acct_versioned %}

#### Object Name
acct_ctr_pst_acct_versioned

#### Object Definition
This table contains the association of the post account start and end dates for the account center and charge account center

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acct_ctr_pst_acct_id & metadata_checksum combination.

#### Primary key
data_acct_ctr_pst_acct_id

#### Tags
    - object_name=acct_ctr_pst_acct
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}