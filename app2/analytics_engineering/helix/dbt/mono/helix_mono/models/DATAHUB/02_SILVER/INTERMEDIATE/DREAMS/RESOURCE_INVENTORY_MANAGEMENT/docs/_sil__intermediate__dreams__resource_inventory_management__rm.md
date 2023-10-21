{% docs sil__intermediate__dreams__resource_inventory_management__rm_cleansed %}

#### Object Name
rm_cleansed

#### Object Definition
This table ties the reservable resource ID to a physical room at the resorts

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_id & metadata_checksum combination.

#### Primary key
data_rsrc_id

#### Tags
    - object_name=rm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rm_versioned %}

#### Object Name
rm_versioned

#### Object Definition
This table ties the reservable resource ID to a physical room at the resorts

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_id & metadata_checksum combination.

#### Primary key
data_rsrc_id

#### Tags
    - object_name=rm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}