{% docs sil__intermediate__dreams__resource_inventory_management__feat_cleansed %}

#### Object Name
feat_cleansed

#### Object Definition
This table associates a unique identifier for the various features of the resort

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_feat_id & metadata_checksum combination.

#### Primary key
data_feat_id

#### Tags
    - object_name=feat
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__feat_versioned %}

#### Object Name
feat_versioned

#### Object Definition
This table associates a unique identifier for the various features of the resort

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_feat_id & metadata_checksum combination.

#### Primary key
data_feat_id

#### Tags
    - object_name=feat
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}