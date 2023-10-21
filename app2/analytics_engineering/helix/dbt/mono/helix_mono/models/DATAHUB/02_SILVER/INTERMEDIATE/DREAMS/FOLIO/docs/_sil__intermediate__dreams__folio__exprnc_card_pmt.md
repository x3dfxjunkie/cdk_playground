{% docs sil__intermediate__dreams__folio__exprnc_card_pmt_cleansed %}

#### Object Name
exprnc_card_pmt_cleansed

#### Object Definition
This table holds Payments that were made by Resort guests at various POS/Dining and that payment becomes a charge the guest is responsible for on their Folio/Bill/Tab that shows what is being processed on the credit card the guest has on file as a settlement method

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pmt_id & metadata_checksum combination.

#### Primary key
data_pmt_id

#### Tags
    - object_name=exprnc_card_pmt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__exprnc_card_pmt_versioned %}

#### Object Name
exprnc_card_pmt_versioned

#### Object Definition
This table holds Payments that were made by Resort guests at various POS/Dining and that payment becomes a charge the guest is responsible for on their Folio/Bill/Tab that shows what is being processed on the credit card the guest has on file as a settlement method

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pmt_id & metadata_checksum combination.

#### Primary key
data_pmt_id

#### Tags
    - object_name=exprnc_card_pmt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}