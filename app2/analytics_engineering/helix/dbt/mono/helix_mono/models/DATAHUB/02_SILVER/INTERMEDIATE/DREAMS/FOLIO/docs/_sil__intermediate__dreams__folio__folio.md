{% docs sil__intermediate__dreams__folio__folio_cleansed %}

#### Object Name
folio_cleansed

#### Object Definition
This table represents which guests are responsible for which Folio balance and if the guest elects to Express check out or Email of this shows what was processed on the credit card the guest has on file as a settlement method

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_folio_id & metadata_checksum combination.

#### Primary key
data_folio_id

#### Tags
    - object_name=folio
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__folio_versioned %}

#### Object Name
folio_versioned

#### Object Definition
This table represents which guests are responsible for which Folio balance and if the guest elects to Express check out or Email of this shows what was processed on the credit card the guest has on file as a settlement method

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_folio_id & metadata_checksum combination.

#### Primary key
data_folio_id

#### Tags
    - object_name=folio
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}