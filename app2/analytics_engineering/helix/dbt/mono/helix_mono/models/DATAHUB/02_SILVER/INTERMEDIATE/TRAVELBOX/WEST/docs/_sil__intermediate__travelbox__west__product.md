{% docs sil__intermediate__travelbox__west__product_cleansed %}

#### Object Name
product_cleansed

#### Object Definition
A system defined table for Travelbox product items name code mapping (FLT:Flights). There is no UI to insert data, have to add manually

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=product
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__product_versioned %}

#### Object Name
product_versioned

#### Object Definition
A system defined table for Travelbox product items name code mapping (FLT:Flights). There is no UI to insert data, have to add manually

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=product
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}