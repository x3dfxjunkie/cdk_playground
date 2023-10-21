{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_own_cleansed %}

#### Object Name
rsrc_own_cleansed

#### Object Definition
This table holds the owner name, from and to dates and adult and child count

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_own_id & metadata_checksum combination.

#### Primary key
data_rsrc_own_id

#### Tags
    - object_name=rsrc_own
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_own_versioned %}

#### Object Name
rsrc_own_versioned

#### Object Definition
This table holds the owner name, from and to dates and adult and child count

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_own_id & metadata_checksum combination.

#### Primary key
data_rsrc_own_id

#### Tags
    - object_name=rsrc_own
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}