{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_req_cleansed %}

#### Object Name
rsrc_asgn_req_cleansed

#### Object Definition
This table provides the the date the inventory is requested for, the rate category, if it&#39;s an all day request or not

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_asgn_req_id & metadata_checksum combination.

#### Primary key
data_rsrc_asgn_req_id

#### Tags
    - object_name=rsrc_asgn_req
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrc_asgn_req_versioned %}

#### Object Name
rsrc_asgn_req_versioned

#### Object Definition
This table provides the the date the inventory is requested for, the rate category, if it&#39;s an all day request or not

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_asgn_req_id & metadata_checksum combination.

#### Primary key
data_rsrc_asgn_req_id

#### Tags
    - object_name=rsrc_asgn_req
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}