{% docs sil__intermediate__dreams__folio__unappl_ppty_cleansed %}

#### Object Name
unappl_ppty_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_unappl_ppty_id & metadata_checksum combination.

#### Primary key
data_unappl_ppty_id

#### Tags
    - object_name=unappl_ppty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__unappl_ppty_versioned %}

#### Object Name
unappl_ppty_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_unappl_ppty_id & metadata_checksum combination.

#### Primary key
data_unappl_ppty_id

#### Tags
    - object_name=unappl_ppty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}