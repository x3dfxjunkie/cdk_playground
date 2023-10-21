{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_invtry_sts_cleansed %}

#### Object Name
rsrc_invtry_sts_cleansed

#### Object Definition
Provides the status and description for rooms put on closed floor or out of inventory

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_invtry_sts_id & metadata_checksum combination.

#### Primary key
data_rsrc_invtry_sts_id

#### Tags
    - object_name=rsrc_invtry_sts
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_invtry_sts_versioned %}

#### Object Name
rsrc_invtry_sts_versioned

#### Object Definition
Provides the status and description for rooms put on closed floor or out of inventory

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_invtry_sts_id & metadata_checksum combination.

#### Primary key
data_rsrc_invtry_sts_id

#### Tags
    - object_name=rsrc_invtry_sts
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}