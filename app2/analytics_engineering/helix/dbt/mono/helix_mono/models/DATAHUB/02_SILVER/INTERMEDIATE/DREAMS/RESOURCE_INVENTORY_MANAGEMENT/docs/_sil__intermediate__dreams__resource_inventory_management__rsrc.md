{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_cleansed %}

#### Object Name
rsrc_cleansed

#### Object Definition
This table holds the inventory of the reservable resources, soon to be room only and not any dining inventory

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_id & metadata_checksum combination.

#### Primary key
data_rsrc_id

#### Tags
    - object_name=rsrc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_versioned %}

#### Object Name
rsrc_versioned

#### Object Definition
This table holds the inventory of the reservable resources, soon to be room only and not any dining inventory

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_id & metadata_checksum combination.

#### Primary key
data_rsrc_id

#### Tags
    - object_name=rsrc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}