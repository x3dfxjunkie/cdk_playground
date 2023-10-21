{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_own_ref_cleansed %}

#### Object Name
rsrc_own_ref_cleansed

#### Object Definition
This table connects resource owner to the reservation IDs:
TP
TPS
TC

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_extnl_own_ref_val, data_rsrc_own_id & metadata_checksum combination.

#### Primary key
data_extnl_own_ref_val, data_rsrc_own_id

#### Tags
    - object_name=rsrc_own_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_own_ref_versioned %}

#### Object Name
rsrc_own_ref_versioned

#### Object Definition
This table connects resource owner to the reservation IDs:
TP
TPS
TC

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_extnl_own_ref_val, data_rsrc_own_id & metadata_checksum combination.

#### Primary key
data_extnl_own_ref_val, data_rsrc_own_id

#### Tags
    - object_name=rsrc_own_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}