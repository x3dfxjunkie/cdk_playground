{% docs sil__intermediate__level__n_wdw__inbound_rest_req_log_cleansed %}

#### Object Name
inbound_rest_req_log_cleansed

#### Object Definition
Log table that captured inbound API request URL and body to Level N from external systems.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_correlation_id, data_req_timestamp & metadata_checksum combination.

#### Primary key
data_correlation_id, data_req_timestamp

#### Tags
    - object_name=inbound_rest_req_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__inbound_rest_req_log_versioned %}

#### Object Name
inbound_rest_req_log_versioned

#### Object Definition
Log table that captured inbound API request URL and body to Level N from external systems.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_correlation_id, data_req_timestamp & metadata_checksum combination.

#### Primary key
data_correlation_id, data_req_timestamp

#### Tags
    - object_name=inbound_rest_req_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}