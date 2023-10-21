{% docs sil__intermediate__dreams__price__acct_rev_cls_t_cleansed %}

#### Object Name
acct_rev_cls_t_cleansed

#### Object Definition
There are over 400 revenue classes associated to a subset of products in a reservation

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acct_rev_cls_id & metadata_checksum combination.

#### Primary key
data_acct_rev_cls_id

#### Tags
    - object_name=acct_rev_cls_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__acct_rev_cls_t_versioned %}

#### Object Name
acct_rev_cls_t_versioned

#### Object Definition
There are over 400 revenue classes associated to a subset of products in a reservation

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acct_rev_cls_id & metadata_checksum combination.

#### Primary key
data_acct_rev_cls_id

#### Tags
    - object_name=acct_rev_cls_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}