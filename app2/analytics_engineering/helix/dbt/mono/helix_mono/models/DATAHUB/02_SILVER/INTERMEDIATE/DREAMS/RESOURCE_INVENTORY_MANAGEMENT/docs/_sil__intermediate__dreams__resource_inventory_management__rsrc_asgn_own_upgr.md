{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_own_upgr_cleansed %}

#### Object Name
rsrc_asgn_own_upgr_cleansed

#### Object Definition
If a room type is upgraded, the new room type will live in this table

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_asgn_ownr_id & metadata_checksum combination.

#### Primary key
data_asgn_ownr_id

#### Tags
    - object_name=rsrc_asgn_own_upgr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_own_upgr_versioned %}

#### Object Name
rsrc_asgn_own_upgr_versioned

#### Object Definition
If a room type is upgraded, the new room type will live in this table

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_asgn_ownr_id & metadata_checksum combination.

#### Primary key
data_asgn_ownr_id

#### Tags
    - object_name=rsrc_asgn_own_upgr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}