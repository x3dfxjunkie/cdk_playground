{% docs sil__intermediate__dreams__folio__folio_item_cleansed %}

#### Object Name
folio_item_cleansed

#### Object Definition
This table ties charge and payment folio items to a Folio

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_folio_item_id & metadata_checksum combination.

#### Primary key
data_folio_item_id

#### Tags
    - object_name=folio_item
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__folio_item_versioned %}

#### Object Name
folio_item_versioned

#### Object Definition
This table ties charge and payment folio items to a Folio

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_folio_item_id & metadata_checksum combination.

#### Primary key
data_folio_item_id

#### Tags
    - object_name=folio_item
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}