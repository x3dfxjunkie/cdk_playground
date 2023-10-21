{% docs sil__intermediate__dreams__accounting__actr_pi_exp_acct_cleansed %}

#### Object Name
actr_pi_exp_acct_cleansed

#### Object Definition
Ties together Post Item account with Post item Expense account. The only expense type as of 6/19/2023 is commission

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acct_ctr_pst_item_exp_acct_id & metadata_checksum combination.

#### Primary key
data_acct_ctr_pst_item_exp_acct_id

#### Tags
    - object_name=actr_pi_exp_acct
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__actr_pi_exp_acct_versioned %}

#### Object Name
actr_pi_exp_acct_versioned

#### Object Definition
Ties together Post Item account with Post item Expense account. The only expense type as of 6/19/2023 is commission

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acct_ctr_pst_item_exp_acct_id & metadata_checksum combination.

#### Primary key
data_acct_ctr_pst_item_exp_acct_id

#### Tags
    - object_name=actr_pi_exp_acct
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}