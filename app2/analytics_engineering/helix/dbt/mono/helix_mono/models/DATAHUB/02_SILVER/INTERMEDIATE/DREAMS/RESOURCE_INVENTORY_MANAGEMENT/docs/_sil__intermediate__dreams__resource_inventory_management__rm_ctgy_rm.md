{% docs sil__intermediate__dreams__resource_inventory_management__rm_ctgy_rm_cleansed %}

#### Object Name
rm_ctgy_rm_cleansed

#### Object Definition
This table ties a room category to the reservable resource ID.
SUITE
VIRTUAL_ROOM
DEFAULT_PARENT
TURN_DOWN
CONCIERGE

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rm_ctgy_nm, data_rsrc_id & metadata_checksum combination.

#### Primary key
data_rm_ctgy_nm, data_rsrc_id

#### Tags
    - object_name=rm_ctgy_rm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rm_ctgy_rm_versioned %}

#### Object Name
rm_ctgy_rm_versioned

#### Object Definition
This table ties a room category to the reservable resource ID.
SUITE
VIRTUAL_ROOM
DEFAULT_PARENT
TURN_DOWN
CONCIERGE

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rm_ctgy_nm, data_rsrc_id & metadata_checksum combination.

#### Primary key
data_rm_ctgy_nm, data_rsrc_id

#### Tags
    - object_name=rm_ctgy_rm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}