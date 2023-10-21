{% docs sil__intermediate__dreams__price__price_sheet_t_cleansed %}

#### Object Name
price_sheet_t_cleansed

#### Object Definition
This table holds component IDs and Names of the price sheet

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_price_sheet_id & metadata_checksum combination.

#### Primary key
data_price_sheet_id

#### Tags
    - object_name=price_sheet_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__price_sheet_t_versioned %}

#### Object Name
price_sheet_t_versioned

#### Object Definition
This table holds component IDs and Names of the price sheet

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_price_sheet_id & metadata_checksum combination.

#### Primary key
data_price_sheet_id

#### Tags
    - object_name=price_sheet_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}