{% docs sil__intermediate__dreams__folio__prod_chrg_cleansed %}

#### Object Name
prod_chrg_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrg_id & metadata_checksum combination.

#### Primary key
data_chrg_id

#### Tags
    - object_name=prod_chrg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__prod_chrg_versioned %}

#### Object Name
prod_chrg_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrg_id & metadata_checksum combination.

#### Primary key
data_chrg_id

#### Tags
    - object_name=prod_chrg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}