{% docs sil__intermediate__dreams__folio__pmt_card_cleansed %}

#### Object Name
pmt_card_cleansed

#### Object Definition
Additional information about credit card payments, including card holder and address

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pmt_card_id & metadata_checksum combination.

#### Primary key
data_pmt_card_id

#### Tags
    - object_name=pmt_card
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__pmt_card_versioned %}

#### Object Name
pmt_card_versioned

#### Object Definition
Additional information about credit card payments, including card holder and address

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pmt_card_id & metadata_checksum combination.

#### Primary key
data_pmt_card_id

#### Tags
    - object_name=pmt_card
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}