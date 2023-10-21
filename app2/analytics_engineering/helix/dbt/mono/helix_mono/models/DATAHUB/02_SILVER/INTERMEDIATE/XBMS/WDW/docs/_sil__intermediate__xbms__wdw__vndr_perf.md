{% docs sil__intermediate__xbms__wdw__vndr_perf_cleansed %}

#### Table Name
vndr_perf_cleansed

#### Table Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_vndr_perf_id & metadata_checksum combination.

#### Primary key
data_vndr_perf_id

#### Tags
    - table_name=vndr_perf
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__vndr_perf_versioned %}

#### Table Name
vndr_perf_versioned

#### Table Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_vndr_perf_id & metadata_checksum combination.

#### Primary key
data_vndr_perf_id

#### Tags
    - table_name=vndr_perf
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}