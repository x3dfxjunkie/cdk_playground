{% docs sil__intermediate__dreams__rooms_fulfillment__res_mgmt_feat_req_cleansed %}

#### Object Name
res_mgmt_feat_req_cleansed

#### Object Definition
This table associated a FEATURE ID to the Reservation Management Request

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_res_mgmt_req_id & metadata_checksum combination.

#### Primary key
data_res_mgmt_req_id

#### Tags
    - object_name=res_mgmt_feat_req
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__res_mgmt_feat_req_versioned %}

#### Object Name
res_mgmt_feat_req_versioned

#### Object Definition
This table associated a FEATURE ID to the Reservation Management Request

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_res_mgmt_req_id & metadata_checksum combination.

#### Primary key
data_res_mgmt_req_id

#### Tags
    - object_name=res_mgmt_feat_req
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}