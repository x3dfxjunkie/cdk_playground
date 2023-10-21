{% docs sil__intermediate__dreams__price__price_def_t_cleansed %}

#### Object Name
price_def_t_cleansed

#### Object Definition
This tables contains the Price Sheet Element ID and the Age Definition ID and pricing information amounts, discount, by age, ticket and tax

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_price_def_id & metadata_checksum combination.

#### Primary key
data_price_def_id

#### Tags
    - object_name=price_def_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__price_def_t_versioned %}

#### Object Name
price_def_t_versioned

#### Object Definition
This tables contains the Price Sheet Element ID and the Age Definition ID and pricing information amounts, discount, by age, ticket and tax

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_price_def_id & metadata_checksum combination.

#### Primary key
data_price_def_id

#### Tags
    - object_name=price_def_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}