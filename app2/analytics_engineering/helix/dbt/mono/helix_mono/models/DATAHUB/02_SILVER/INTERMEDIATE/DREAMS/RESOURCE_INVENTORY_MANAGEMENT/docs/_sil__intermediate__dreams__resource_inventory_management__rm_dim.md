{% docs sil__intermediate__dreams__resource_inventory_management__rm_dim_cleansed %}

#### Object Name
rm_dim_cleansed

#### Object Definition
This table provides the structure type of a reservable resource:
ROOM
BALCONY

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_id, data_struct_typ_nm & metadata_checksum combination.

#### Primary key
data_rsrc_id, data_struct_typ_nm

#### Tags
    - object_name=rm_dim
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rm_dim_versioned %}

#### Object Name
rm_dim_versioned

#### Object Definition
This table provides the structure type of a reservable resource:
ROOM
BALCONY

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_id, data_struct_typ_nm & metadata_checksum combination.

#### Primary key
data_rsrc_id, data_struct_typ_nm

#### Tags
    - object_name=rm_dim
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}