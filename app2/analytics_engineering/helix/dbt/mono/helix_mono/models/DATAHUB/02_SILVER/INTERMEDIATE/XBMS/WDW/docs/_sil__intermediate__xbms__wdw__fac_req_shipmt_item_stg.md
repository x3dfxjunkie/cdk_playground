{% docs sil__intermediate__xbms__wdw__fac_req_shipmt_item_stg_cleansed %}

#### Table Name
fac_req_shipmt_item_stg_cleansed

#### Table Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_fac_req_shipmt_item_stg_id & metadata_checksum combination.

#### Primary key
data_fac_req_shipmt_item_stg_id

#### Tags
    - table_name=fac_req_shipmt_item_stg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__fac_req_shipmt_item_stg_versioned %}

#### Table Name
fac_req_shipmt_item_stg_versioned

#### Table Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_fac_req_shipmt_item_stg_id & metadata_checksum combination.

#### Primary key
data_fac_req_shipmt_item_stg_id

#### Tags
    - table_name=fac_req_shipmt_item_stg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}