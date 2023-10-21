{% docs sil__intermediate__xbms__wdw__pii_arch_exprnc_band_lnk_cleansed %}

#### Table Name
pii_arch_exprnc_band_lnk_cleansed

#### Table Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_exprnc_band_lnk_id & metadata_checksum combination.

#### Primary key
data_exprnc_band_lnk_id

#### Tags
    - table_name=pii_arch_exprnc_band_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__pii_arch_exprnc_band_lnk_versioned %}

#### Table Name
pii_arch_exprnc_band_lnk_versioned

#### Table Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_exprnc_band_lnk_id & metadata_checksum combination.

#### Primary key
data_exprnc_band_lnk_id

#### Tags
    - table_name=pii_arch_exprnc_band_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}