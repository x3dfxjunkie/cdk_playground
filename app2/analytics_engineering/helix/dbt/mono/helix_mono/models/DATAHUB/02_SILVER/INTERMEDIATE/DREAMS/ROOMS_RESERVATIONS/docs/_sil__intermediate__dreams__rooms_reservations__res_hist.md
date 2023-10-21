{% docs sil__intermediate__dreams__rooms_reservations__res_hist_cleansed %}

#### Object Name
res_hist_cleansed

#### Object Definition
This is a copy of the reservation history that is shown online, it is created by the source.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_res_hist_id & metadata_checksum combination.

#### Primary key
data_res_hist_id

#### Tags
    - object_name=res_hist
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__res_hist_versioned %}

#### Object Name
res_hist_versioned

#### Object Definition
This is a copy of the reservation history that is shown online, it is created by the source.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_res_hist_id & metadata_checksum combination.

#### Primary key
data_res_hist_id

#### Tags
    - object_name=res_hist
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}