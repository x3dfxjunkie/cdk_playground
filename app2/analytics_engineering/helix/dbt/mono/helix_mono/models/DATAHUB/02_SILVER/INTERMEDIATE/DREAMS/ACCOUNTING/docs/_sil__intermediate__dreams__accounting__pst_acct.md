{% docs sil__intermediate__dreams__accounting__pst_acct_cleansed %}

#### Object Name
pst_acct_cleansed

#### Object Definition
The post account type associated to the post account name
Posting Item
Payment Method

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pst_acct_id & metadata_checksum combination.

#### Primary key
data_pst_acct_id

#### Tags
    - object_name=pst_acct
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__pst_acct_versioned %}

#### Object Name
pst_acct_versioned

#### Object Definition
The post account type associated to the post account name
Posting Item
Payment Method

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pst_acct_id & metadata_checksum combination.

#### Primary key
data_pst_acct_id

#### Tags
    - object_name=pst_acct
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}