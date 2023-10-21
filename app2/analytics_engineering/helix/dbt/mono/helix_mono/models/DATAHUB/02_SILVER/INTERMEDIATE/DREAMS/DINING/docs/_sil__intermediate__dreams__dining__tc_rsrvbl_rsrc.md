{% docs sil__intermediate__dreams__dining__tc_rsrvbl_rsrc_cleansed %}

#### Object Name
tc_rsrvbl_rsrc_cleansed

#### Object Definition
This table ties the reservable resource to certain travel components, it&#39;s the inventory item for that component ie: room type, table top type for Scheduled Events/Dining

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_rsrvbl_rsrc_id & metadata_checksum combination.

#### Primary key
data_tc_rsrvbl_rsrc_id

#### Tags
    - object_name=tc_rsrvbl_rsrc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__tc_rsrvbl_rsrc_versioned %}

#### Object Name
tc_rsrvbl_rsrc_versioned

#### Object Definition
This table ties the reservable resource to certain travel components, it&#39;s the inventory item for that component ie: room type, table top type for Scheduled Events/Dining

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_rsrvbl_rsrc_id & metadata_checksum combination.

#### Primary key
data_tc_rsrvbl_rsrc_id

#### Tags
    - object_name=tc_rsrvbl_rsrc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}