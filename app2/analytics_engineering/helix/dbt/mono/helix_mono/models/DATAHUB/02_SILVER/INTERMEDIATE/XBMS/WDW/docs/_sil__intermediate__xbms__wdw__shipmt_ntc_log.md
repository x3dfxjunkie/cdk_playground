{% docs sil__intermediate__xbms__wdw__shipmt_ntc_log_cleansed %}

#### Table Name
shipmt_ntc_log_cleansed

#### Table Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_shipmt_ntc_log_id & metadata_checksum combination.

#### Primary key
data_shipmt_ntc_log_id

#### Tags
    - table_name=shipmt_ntc_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__shipmt_ntc_log_versioned %}

#### Table Name
shipmt_ntc_log_versioned

#### Table Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_shipmt_ntc_log_id & metadata_checksum combination.

#### Primary key
data_shipmt_ntc_log_id

#### Tags
    - table_name=shipmt_ntc_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}