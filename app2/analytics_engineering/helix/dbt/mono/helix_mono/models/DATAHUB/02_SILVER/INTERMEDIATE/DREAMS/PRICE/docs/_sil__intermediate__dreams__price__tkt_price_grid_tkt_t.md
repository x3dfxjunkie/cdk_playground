{% docs sil__intermediate__dreams__price__tkt_price_grid_tkt_t_cleansed %}

#### Object Name
tkt_price_grid_tkt_t_cleansed

#### Object Definition
Ties ticket ID to the Price Grid ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tkt_id, data_tkt_price_grid_id & metadata_checksum combination.

#### Primary key
data_tkt_id, data_tkt_price_grid_id

#### Tags
    - object_name=tkt_price_grid_tkt_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__tkt_price_grid_tkt_t_versioned %}

#### Object Name
tkt_price_grid_tkt_t_versioned

#### Object Definition
Ties ticket ID to the Price Grid ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tkt_id, data_tkt_price_grid_id & metadata_checksum combination.

#### Primary key
data_tkt_id, data_tkt_price_grid_id

#### Tags
    - object_name=tkt_price_grid_tkt_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}