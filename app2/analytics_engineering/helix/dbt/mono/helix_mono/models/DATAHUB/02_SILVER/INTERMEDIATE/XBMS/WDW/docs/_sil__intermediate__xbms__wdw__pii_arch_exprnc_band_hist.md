{% docs sil__intermediate__xbms__wdw__pii_arch_exprnc_band_hist_cleansed %}

#### Object Name
pii_arch_exprnc_band_hist_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pii_arch_exprnc_band_hist_id & metadata_checksum combination.

#### Primary key
data_pii_arch_exprnc_band_hist_id

#### Tags
    - object_name=pii_arch_exprnc_band_hist
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__pii_arch_exprnc_band_hist_versioned %}

#### Object Name
pii_arch_exprnc_band_hist_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pii_arch_exprnc_band_hist_id & metadata_checksum combination.

#### Primary key
data_pii_arch_exprnc_band_hist_id

#### Tags
    - object_name=pii_arch_exprnc_band_hist
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}