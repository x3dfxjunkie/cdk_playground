{% docs sil__intermediate__dreams__resource_inventory_management__asgn_ownr_guar_feat_cleansed %}

#### Object Name
asgn_ownr_guar_feat_cleansed

#### Object Definition
This table links the assigned owner ID to Feature IDs that are guaranteed to be fulfilled

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_asgn_ownr_id, data_feat_id & metadata_checksum combination.

#### Primary key
data_asgn_ownr_id, data_feat_id

#### Tags
    - object_name=asgn_ownr_guar_feat
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__asgn_ownr_guar_feat_versioned %}

#### Object Name
asgn_ownr_guar_feat_versioned

#### Object Definition
This table links the assigned owner ID to Feature IDs that are guaranteed to be fulfilled

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_asgn_ownr_id, data_feat_id & metadata_checksum combination.

#### Primary key
data_asgn_ownr_id, data_feat_id

#### Tags
    - object_name=asgn_ownr_guar_feat
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}