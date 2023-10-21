{% docs sil__intermediate__level__n_wdw__mm_ticket_details_cleansed %}

#### Object Name
mm_ticket_details_cleansed

#### Object Definition
Table containing ticket products, with the code, price, and description that include memory maker.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=mm_ticket_details
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__mm_ticket_details_versioned %}

#### Object Name
mm_ticket_details_versioned

#### Object Definition
Table containing ticket products, with the code, price, and description that include memory maker.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=mm_ticket_details
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}