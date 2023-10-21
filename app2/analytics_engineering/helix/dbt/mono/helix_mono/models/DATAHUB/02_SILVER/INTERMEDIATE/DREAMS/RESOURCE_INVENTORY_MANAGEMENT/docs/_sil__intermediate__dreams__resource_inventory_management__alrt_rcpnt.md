{% docs sil__intermediate__dreams__resource_inventory_management__alrt_rcpnt_cleansed %}

#### Object Name
alrt_rcpnt_cleansed

#### Object Definition
This table identifies the recipients of alerts regarding the resource inventory status. The recipients:
HOUSEKEEPING_MANAGER
RESORT_MANAGER
ROOM_ASSIGNER

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_alrt_rcpnt_id & metadata_checksum combination.

#### Primary key
data_alrt_rcpnt_id

#### Tags
    - object_name=alrt_rcpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__alrt_rcpnt_versioned %}

#### Object Name
alrt_rcpnt_versioned

#### Object Definition
This table identifies the recipients of alerts regarding the resource inventory status. The recipients:
HOUSEKEEPING_MANAGER
RESORT_MANAGER
ROOM_ASSIGNER

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_alrt_rcpnt_id & metadata_checksum combination.

#### Primary key
data_alrt_rcpnt_id

#### Tags
    - object_name=alrt_rcpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}