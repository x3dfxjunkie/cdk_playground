{% docs sil__intermediate__xbms__wdw__exprnc_band_rl_actvy_cleansed %}

#### Table Name
exprnc_band_rl_actvy_cleansed

#### Table Definition
Contains Experience Band RL Activity Details

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_exprnc_band_rl_actvy_id & metadata_checksum combination.

#### Primary key
data_exprnc_band_rl_actvy_id

#### Tags
    - table_name=exprnc_band_rl_actvy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__exprnc_band_rl_actvy_versioned %}

#### Table Name
exprnc_band_rl_actvy_versioned

#### Table Definition
Contains Experience Band RL Activity Details

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_exprnc_band_rl_actvy_id & metadata_checksum combination.

#### Primary key
data_exprnc_band_rl_actvy_id

#### Tags
    - table_name=exprnc_band_rl_actvy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}