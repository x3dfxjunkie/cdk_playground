{% docs sil__intermediate__xbms__wdw__fflmt_procurmt_rsn_config_cleansed %}

#### Object Name
fflmt_procurmt_rsn_config_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_fflmt_procurmt_rsn_config_id & metadata_checksum combination.

#### Primary key
data_fflmt_procurmt_rsn_config_id

#### Tags
    - object_name=fflmt_procurmt_rsn_config
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__fflmt_procurmt_rsn_config_versioned %}

#### Object Name
fflmt_procurmt_rsn_config_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_fflmt_procurmt_rsn_config_id & metadata_checksum combination.

#### Primary key
data_fflmt_procurmt_rsn_config_id

#### Tags
    - object_name=fflmt_procurmt_rsn_config
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}