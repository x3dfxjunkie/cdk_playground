{% docs sil__intermediate__dreams__resource_inventory_management__cnct_rm_lnk_cleansed %}

#### Object Name
cnct_rm_lnk_cleansed

#### Object Definition
This table holds the IDs of rooms that connect

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cnctd_rsrc_id, data_cnctg_rsrc_id & metadata_checksum combination.

#### Primary key
data_cnctd_rsrc_id, data_cnctg_rsrc_id

#### Tags
    - object_name=cnct_rm_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__cnct_rm_lnk_versioned %}

#### Object Name
cnct_rm_lnk_versioned

#### Object Definition
This table holds the IDs of rooms that connect

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cnctd_rsrc_id, data_cnctg_rsrc_id & metadata_checksum combination.

#### Primary key
data_cnctd_rsrc_id, data_cnctg_rsrc_id

#### Tags
    - object_name=cnct_rm_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}