{% docs sil__intermediate__dreams__price__price_grid_t_cleansed %}

#### Object Name
price_grid_t_cleansed

#### Object Definition
This price grid description of tickets and &#39;other&#39; products that are more associated to scheduled events

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_price_grid_id & metadata_checksum combination.

#### Primary key
data_price_grid_id

#### Tags
    - object_name=price_grid_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__price_grid_t_versioned %}

#### Object Name
price_grid_t_versioned

#### Object Definition
This price grid description of tickets and &#39;other&#39; products that are more associated to scheduled events

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_price_grid_id & metadata_checksum combination.

#### Primary key
data_price_grid_id

#### Tags
    - object_name=price_grid_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}