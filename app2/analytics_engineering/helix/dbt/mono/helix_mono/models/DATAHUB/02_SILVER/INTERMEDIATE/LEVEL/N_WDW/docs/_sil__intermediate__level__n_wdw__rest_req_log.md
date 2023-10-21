{% docs sil__intermediate__level__n_wdw__rest_req_log_cleansed %}

#### Object Name
rest_req_log_cleansed

#### Object Definition
Log table for Level N that tracks Restful requests to Level N API.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_correlation_id, data_req_timestamp_id & metadata_checksum combination.

#### Primary key
data_correlation_id, data_req_timestamp_id

#### Tags
    - object_name=rest_req_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__rest_req_log_versioned %}

#### Object Name
rest_req_log_versioned

#### Object Definition
Log table for Level N that tracks Restful requests to Level N API.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_correlation_id, data_req_timestamp_id & metadata_checksum combination.

#### Primary key
data_correlation_id, data_req_timestamp_id

#### Tags
    - object_name=rest_req_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}