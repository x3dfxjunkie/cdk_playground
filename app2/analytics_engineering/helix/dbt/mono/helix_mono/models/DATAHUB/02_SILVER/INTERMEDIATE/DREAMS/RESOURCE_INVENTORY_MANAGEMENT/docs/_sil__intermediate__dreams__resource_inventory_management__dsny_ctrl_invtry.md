{% docs sil__intermediate__dreams__resource_inventory_management__dsny_ctrl_invtry_cleansed %}

#### Object Name
dsny_ctrl_invtry_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_asgn_ownr_id & metadata_checksum combination.

#### Primary key
data_asgn_ownr_id

#### Tags
    - object_name=dsny_ctrl_invtry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__dsny_ctrl_invtry_versioned %}

#### Object Name
dsny_ctrl_invtry_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_asgn_ownr_id & metadata_checksum combination.

#### Primary key
data_asgn_ownr_id

#### Tags
    - object_name=dsny_ctrl_invtry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}