{% docs sil__intermediate__dreams__resource_inventory_management__invtry_req_cleansed %}

#### Object Name
invtry_req_cleansed

#### Object Definition
This table tracks the history of inventory requests of
OUT_OF_INVENTORY
CLOSED_FLOOR

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_invtry_req_id & metadata_checksum combination.

#### Primary key
data_rsrc_invtry_req_id

#### Tags
    - object_name=invtry_req
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__invtry_req_versioned %}

#### Object Name
invtry_req_versioned

#### Object Definition
This table tracks the history of inventory requests of
OUT_OF_INVENTORY
CLOSED_FLOOR

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_invtry_req_id & metadata_checksum combination.

#### Primary key
data_rsrc_invtry_req_id

#### Tags
    - object_name=invtry_req
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}