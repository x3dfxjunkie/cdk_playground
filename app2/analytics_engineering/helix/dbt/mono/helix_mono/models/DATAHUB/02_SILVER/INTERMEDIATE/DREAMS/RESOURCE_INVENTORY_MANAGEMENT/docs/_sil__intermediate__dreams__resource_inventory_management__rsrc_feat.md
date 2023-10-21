{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_feat_cleansed %}

#### Object Name
rsrc_feat_cleansed

#### Object Definition
This table connects the reservable resource and the feature IDs associated to it

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_feat_id, data_rsrc_id & metadata_checksum combination.

#### Primary key
data_feat_id, data_rsrc_id

#### Tags
    - object_name=rsrc_feat
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_feat_versioned %}

#### Object Name
rsrc_feat_versioned

#### Object Definition
This table connects the reservable resource and the feature IDs associated to it

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_feat_id, data_rsrc_id & metadata_checksum combination.

#### Primary key
data_feat_id, data_rsrc_id

#### Tags
    - object_name=rsrc_feat
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}