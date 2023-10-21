{% docs sil__intermediate__dreams__folio__folio_pmt_cleansed %}

#### Object Name
folio_pmt_cleansed

#### Object Definition
This table ties the payment ID to Folio Settlement Method and the Charge Group Folio ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pmt_id & metadata_checksum combination.

#### Primary key
data_pmt_id

#### Tags
    - object_name=folio_pmt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__folio_pmt_versioned %}

#### Object Name
folio_pmt_versioned

#### Object Definition
This table ties the payment ID to Folio Settlement Method and the Charge Group Folio ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pmt_id & metadata_checksum combination.

#### Primary key
data_pmt_id

#### Tags
    - object_name=folio_pmt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}