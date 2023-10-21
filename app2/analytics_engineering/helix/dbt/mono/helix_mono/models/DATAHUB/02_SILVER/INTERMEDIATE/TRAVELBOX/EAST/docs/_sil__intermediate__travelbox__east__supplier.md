{% docs sil__intermediate__travelbox__east__supplier_cleansed %}

#### Object Name
supplier_cleansed

#### Object Definition
Pass through view of supplier information which contains resorts

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_supplier_id & metadata_checksum combination.

#### Primary key
data_supplier_id

#### Tags
    - object_name=supplier
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__supplier_versioned %}

#### Object Name
supplier_versioned

#### Object Definition
Pass through view of supplier information which contains resorts

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_supplier_id & metadata_checksum combination.

#### Primary key
data_supplier_id

#### Tags
    - object_name=supplier
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}