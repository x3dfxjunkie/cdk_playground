{% docs sil__intermediate__level__n_wdw__extnl_acct_lnk_cleansed %}

#### Object Name
extnl_acct_lnk_cleansed

#### Object Definition
Contains external account links from the GAM Keyring (admission-link-id, transactional-guest-id) that are sent in by the source systems (DREAMS, SNAPP, TITUS) when they first make the request to level N entitlement to make the entitlement.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_extnl_acct_lnk_id & metadata_checksum combination.

#### Primary key
data_extnl_acct_lnk_id

#### Tags
    - object_name=extnl_acct_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__extnl_acct_lnk_versioned %}

#### Object Name
extnl_acct_lnk_versioned

#### Object Definition
Contains external account links from the GAM Keyring (admission-link-id, transactional-guest-id) that are sent in by the source systems (DREAMS, SNAPP, TITUS) when they first make the request to level N entitlement to make the entitlement.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_extnl_acct_lnk_id & metadata_checksum combination.

#### Primary key
data_extnl_acct_lnk_id

#### Tags
    - object_name=extnl_acct_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}