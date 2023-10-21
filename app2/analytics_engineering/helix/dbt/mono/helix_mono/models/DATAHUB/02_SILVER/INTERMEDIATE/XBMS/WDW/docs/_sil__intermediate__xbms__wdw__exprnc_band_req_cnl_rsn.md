{% docs sil__intermediate__xbms__wdw__exprnc_band_req_cnl_rsn_cleansed %}

#### Object Name
exprnc_band_req_cnl_rsn_cleansed

#### Object Definition
Table containing RAPI cancel codes for cancellation events.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_exprnc_band_req_cnl_rsn_id & metadata_checksum combination.

#### Primary key
data_exprnc_band_req_cnl_rsn_id

#### Tags
    - object_name=exprnc_band_req_cnl_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__exprnc_band_req_cnl_rsn_versioned %}

#### Object Name
exprnc_band_req_cnl_rsn_versioned

#### Object Definition
Table containing RAPI cancel codes for cancellation events.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_exprnc_band_req_cnl_rsn_id & metadata_checksum combination.

#### Primary key
data_exprnc_band_req_cnl_rsn_id

#### Tags
    - object_name=exprnc_band_req_cnl_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}