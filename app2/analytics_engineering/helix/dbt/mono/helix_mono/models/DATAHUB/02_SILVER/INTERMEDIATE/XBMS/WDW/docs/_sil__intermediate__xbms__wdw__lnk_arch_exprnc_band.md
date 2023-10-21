{% docs sil__intermediate__xbms__wdw__lnk_arch_exprnc_band_cleansed %}

#### Object Name
lnk_arch_exprnc_band_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lnk_arch_exprnc_band_id & metadata_checksum combination.

#### Primary key
data_lnk_arch_exprnc_band_id

#### Tags
    - object_name=lnk_arch_exprnc_band
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__lnk_arch_exprnc_band_versioned %}

#### Object Name
lnk_arch_exprnc_band_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lnk_arch_exprnc_band_id & metadata_checksum combination.

#### Primary key
data_lnk_arch_exprnc_band_id

#### Tags
    - object_name=lnk_arch_exprnc_band
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}