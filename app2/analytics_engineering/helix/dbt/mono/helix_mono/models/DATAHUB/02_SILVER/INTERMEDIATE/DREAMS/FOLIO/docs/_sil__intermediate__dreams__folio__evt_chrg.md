{% docs sil__intermediate__dreams__folio__evt_chrg_cleansed %}

#### Object Name
evt_chrg_cleansed

#### Object Definition
This table holds Charges that are related to Events which are related to Group/Convention guests

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_evt_chrg_id & metadata_checksum combination.

#### Primary key
data_evt_chrg_id

#### Tags
    - object_name=evt_chrg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__evt_chrg_versioned %}

#### Object Name
evt_chrg_versioned

#### Object Definition
This table holds Charges that are related to Events which are related to Group/Convention guests

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_evt_chrg_id & metadata_checksum combination.

#### Primary key
data_evt_chrg_id

#### Tags
    - object_name=evt_chrg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}