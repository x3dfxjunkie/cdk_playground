{% docs sil__intermediate__dreams__rooms_fulfillment__res_mgmt_msg_cleansed %}

#### Object Name
res_mgmt_msg_cleansed

#### Object Definition
This table indicates if a guests package or message was delivered.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_res_mgmt_req_id & metadata_checksum combination.

#### Primary key
data_res_mgmt_req_id

#### Tags
    - object_name=res_mgmt_msg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__res_mgmt_msg_versioned %}

#### Object Name
res_mgmt_msg_versioned

#### Object Definition
This table indicates if a guests package or message was delivered.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_res_mgmt_req_id & metadata_checksum combination.

#### Primary key
data_res_mgmt_req_id

#### Tags
    - object_name=res_mgmt_msg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}