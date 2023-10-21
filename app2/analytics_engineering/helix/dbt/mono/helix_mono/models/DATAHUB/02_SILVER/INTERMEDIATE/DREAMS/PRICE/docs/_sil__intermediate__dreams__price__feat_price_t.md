{% docs sil__intermediate__dreams__price__feat_price_t_cleansed %}

#### Object Name
feat_price_t_cleansed

#### Object Definition
Features and Products associated to a price sheet

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_feat_price_id & metadata_checksum combination.

#### Primary key
data_feat_price_id

#### Tags
    - object_name=feat_price_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__feat_price_t_versioned %}

#### Object Name
feat_price_t_versioned

#### Object Definition
Features and Products associated to a price sheet

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_feat_price_id & metadata_checksum combination.

#### Primary key
data_feat_price_id

#### Tags
    - object_name=feat_price_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}