{% docs sil__intermediate__level__n_wdw__lvl_n_feat_prod_cleansed %}

#### Object Name
lvl_n_feat_prod_cleansed

#### Object Definition
Mapping table between the Level N feature product ID, the content cache ID, and the feature ID.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_feat_prod_lnk_id & metadata_checksum combination.

#### Primary key
data_lvl_n_feat_prod_lnk_id

#### Tags
    - object_name=lvl_n_feat_prod
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_feat_prod_versioned %}

#### Object Name
lvl_n_feat_prod_versioned

#### Object Definition
Mapping table between the Level N feature product ID, the content cache ID, and the feature ID.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_feat_prod_lnk_id & metadata_checksum combination.

#### Primary key
data_lvl_n_feat_prod_lnk_id

#### Tags
    - object_name=lvl_n_feat_prod
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}