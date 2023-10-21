{% docs sil__intermediate__das__wdw__lnk_cleansed %}

#### Object Name
lnk_cleansed

#### Object Definition
A list of all Guests that were created for entitlements. Contains Guest PII, such as first name and last name, of Guest associated to account link id.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lnk_id & metadata_checksum combination.

#### Primary key
data_lnk_id

#### Tags
    - object_name=lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__das__wdw__lnk_versioned %}

#### Object Name
lnk_versioned

#### Object Definition
A list of all Guests that were created for entitlements. Contains Guest PII, such as first name and last name, of Guest associated to account link id.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lnk_id & metadata_checksum combination.

#### Primary key
data_lnk_id

#### Tags
    - object_name=lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}