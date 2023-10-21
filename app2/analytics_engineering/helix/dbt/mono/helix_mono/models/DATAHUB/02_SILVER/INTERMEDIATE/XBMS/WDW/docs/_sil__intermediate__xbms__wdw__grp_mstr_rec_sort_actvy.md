{% docs sil__intermediate__xbms__wdw__grp_mstr_rec_sort_actvy_cleansed %}

#### Object Name
grp_mstr_rec_sort_actvy_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_grp_mstr_rec_sort_actvy_id & metadata_checksum combination.

#### Primary key
data_grp_mstr_rec_sort_actvy_id

#### Tags
    - object_name=grp_mstr_rec_sort_actvy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__grp_mstr_rec_sort_actvy_versioned %}

#### Object Name
grp_mstr_rec_sort_actvy_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_grp_mstr_rec_sort_actvy_id & metadata_checksum combination.

#### Primary key
data_grp_mstr_rec_sort_actvy_id

#### Tags
    - object_name=grp_mstr_rec_sort_actvy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}