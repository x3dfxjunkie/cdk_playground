{% docs sil__intermediate__dreams__resource_inventory_management__cmptr_wrkstn_cleansed %}

#### Object Name
cmptr_wrkstn_cleansed

#### Object Definition
This table provides information regarding the different technical devices used when interacting with guests 

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cmptr_wrkstn_id & metadata_checksum combination.

#### Primary key
data_cmptr_wrkstn_id

#### Tags
    - object_name=cmptr_wrkstn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__cmptr_wrkstn_versioned %}

#### Object Name
cmptr_wrkstn_versioned

#### Object Definition
This table provides information regarding the different technical devices used when interacting with guests 

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cmptr_wrkstn_id & metadata_checksum combination.

#### Primary key
data_cmptr_wrkstn_id

#### Tags
    - object_name=cmptr_wrkstn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}