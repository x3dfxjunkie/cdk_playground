{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_typ_cleansed %}

#### Object Name
rsrc_typ_cleansed

#### Object Definition
List of types of Resources:
TABLE
ROOM
SCHEDULE_EVENTS

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_typ_nm & metadata_checksum combination.

#### Primary key
data_rsrc_typ_nm

#### Tags
    - object_name=rsrc_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_typ_versioned %}

#### Object Name
rsrc_typ_versioned

#### Object Definition
List of types of Resources:
TABLE
ROOM
SCHEDULE_EVENTS

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_typ_nm & metadata_checksum combination.

#### Primary key
data_rsrc_typ_nm

#### Tags
    - object_name=rsrc_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}