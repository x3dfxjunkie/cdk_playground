{% docs sil__intermediate__level__n_wdw__inbound_rest_resp_log_cleansed %}

#### Object Name
inbound_rest_resp_log_cleansed

#### Object Definition
Log table that captures API responses from Level N to external systems.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_correlation_id, data_resp_timestamp & metadata_checksum combination.

#### Primary key
data_correlation_id, data_resp_timestamp

#### Tags
    - object_name=inbound_rest_resp_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__inbound_rest_resp_log_versioned %}

#### Object Name
inbound_rest_resp_log_versioned

#### Object Definition
Log table that captures API responses from Level N to external systems.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_correlation_id, data_resp_timestamp & metadata_checksum combination.

#### Primary key
data_correlation_id, data_resp_timestamp

#### Tags
    - object_name=inbound_rest_resp_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}