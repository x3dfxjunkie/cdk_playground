{% docs sil__intermediate__level__n_wdw__app_config_dtls_cleansed %}

#### Object Name
app_config_dtls_cleansed

#### Object Definition
Table containing application configuration IDs and their values.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_app_config_dtls_id & metadata_checksum combination.

#### Primary key
data_app_config_dtls_id

#### Tags
    - object_name=app_config_dtls
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__app_config_dtls_versioned %}

#### Object Name
app_config_dtls_versioned

#### Object Definition
Table containing application configuration IDs and their values.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_app_config_dtls_id & metadata_checksum combination.

#### Primary key
data_app_config_dtls_id

#### Tags
    - object_name=app_config_dtls
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}