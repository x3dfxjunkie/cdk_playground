{% docs sil__intermediate__xbms__wdw__suplmnt_log_tbl_cleansed %}

#### Table Name
suplmnt_log_tbl_cleansed

#### Table Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_suplmnt_log_tbl_nm & metadata_checksum combination.

#### Primary key
data_suplmnt_log_tbl_nm

#### Tags
    - table_name=suplmnt_log_tbl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__suplmnt_log_tbl_versioned %}

#### Table Name
suplmnt_log_tbl_versioned

#### Table Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_suplmnt_log_tbl_nm & metadata_checksum combination.

#### Primary key
data_suplmnt_log_tbl_nm

#### Tags
    - table_name=suplmnt_log_tbl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}