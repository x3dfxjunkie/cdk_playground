{% docs sil__intermediate__level__n_wdw__mmdp_ticket_price_cleansed %}

#### Object Name
mmdp_ticket_price_cleansed

#### Object Definition
Reference table containing memory maker day pass codes and their ticket price and description.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=mmdp_ticket_price
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__mmdp_ticket_price_versioned %}

#### Object Name
mmdp_ticket_price_versioned

#### Object Definition
Reference table containing memory maker day pass codes and their ticket price and description.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=mmdp_ticket_price
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}