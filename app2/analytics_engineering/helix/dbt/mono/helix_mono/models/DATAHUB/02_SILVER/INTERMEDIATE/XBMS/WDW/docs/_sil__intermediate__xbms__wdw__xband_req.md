{% docs sil__intermediate__xbms__wdw__xband_req_cleansed %}

#### Table Name
xband_req_cleansed

#### Table Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_xband_req_id & metadata_checksum combination.

#### Primary key
data_xband_req_id

#### Tags
    - table_name=xband_req
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__xband_req_versioned %}

#### Table Name
xband_req_versioned

#### Table Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_xband_req_id & metadata_checksum combination.

#### Primary key
data_xband_req_id

#### Tags
    - table_name=xband_req
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}