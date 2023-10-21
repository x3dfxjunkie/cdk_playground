{% docs sil__intermediate__xbms__wdw__build_band_sku_actvy_cleansed %}

#### Object Name
build_band_sku_actvy_cleansed

#### Object Definition
Table that tracks activity across build a band SKUs.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_build_band_sku_actvy_id & metadata_checksum combination.

#### Primary key
data_build_band_sku_actvy_id

#### Tags
    - object_name=build_band_sku_actvy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__build_band_sku_actvy_versioned %}

#### Object Name
build_band_sku_actvy_versioned

#### Object Definition
Table that tracks activity across build a band SKUs.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_build_band_sku_actvy_id & metadata_checksum combination.

#### Primary key
data_build_band_sku_actvy_id

#### Tags
    - object_name=build_band_sku_actvy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}