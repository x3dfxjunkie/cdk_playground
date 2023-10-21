{% docs sil__intermediate__level__n_wdw__lvl_n_enttl_cleansed %}

#### Object Name
lvl_n_enttl_cleansed

#### Object Definition
Captures details about the sale of a Level N Entitlement to a Guest, and identifies attributes such as a specific product and pricing.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_enttl_id & metadata_checksum combination.

#### Primary key
data_lvl_n_enttl_id

#### Tags
    - object_name=lvl_n_enttl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_enttl_versioned %}

#### Object Name
lvl_n_enttl_versioned

#### Object Definition
Captures details about the sale of a Level N Entitlement to a Guest, and identifies attributes such as a specific product and pricing.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_enttl_id & metadata_checksum combination.

#### Primary key
data_lvl_n_enttl_id

#### Tags
    - object_name=lvl_n_enttl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}