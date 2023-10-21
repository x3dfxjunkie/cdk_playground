{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_ownr_cleansed %}

#### Object Name
rsrc_asgn_ownr_cleansed

#### Object Definition
This table assigns the owner to a room type indicated by the resource inventory type ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_asgn_ownr_id & metadata_checksum combination.

#### Primary key
data_asgn_ownr_id

#### Tags
    - object_name=rsrc_asgn_ownr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_ownr_versioned %}

#### Object Name
rsrc_asgn_ownr_versioned

#### Object Definition
This table assigns the owner to a room type indicated by the resource inventory type ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_asgn_ownr_id & metadata_checksum combination.

#### Primary key
data_asgn_ownr_id

#### Tags
    - object_name=rsrc_asgn_ownr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}