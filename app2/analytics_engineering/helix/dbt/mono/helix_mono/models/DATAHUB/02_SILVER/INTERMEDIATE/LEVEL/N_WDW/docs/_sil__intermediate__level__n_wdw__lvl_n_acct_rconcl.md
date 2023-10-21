{% docs sil__intermediate__level__n_wdw__lvl_n_acct_rconcl_cleansed %}

#### Object Name
lvl_n_acct_rconcl_cleansed

#### Object Definition
Contains reference for external account links to level n link id.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_extnl_acct_lnk_id & metadata_checksum combination.

#### Primary key
data_extnl_acct_lnk_id

#### Tags
    - object_name=lvl_n_acct_rconcl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_acct_rconcl_versioned %}

#### Object Name
lvl_n_acct_rconcl_versioned

#### Object Definition
Contains reference for external account links to level n link id.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_extnl_acct_lnk_id & metadata_checksum combination.

#### Primary key
data_extnl_acct_lnk_id

#### Tags
    - object_name=lvl_n_acct_rconcl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}