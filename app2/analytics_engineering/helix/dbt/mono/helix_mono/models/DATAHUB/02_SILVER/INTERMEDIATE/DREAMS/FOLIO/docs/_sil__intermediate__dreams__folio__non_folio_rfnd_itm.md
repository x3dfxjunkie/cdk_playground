{% docs sil__intermediate__dreams__folio__non_folio_rfnd_itm_cleansed %}

#### Object Name
non_folio_rfnd_itm_cleansed

#### Object Definition
This table tracks refunds that occur at the Front Desk for items that would not be included in a guest folio.NON_FOLIO_RFND_ITEM_TYP_NM, Parking Refunds, Other Refunds, Machine Refunds

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_non_folio_rfnd_item_id & metadata_checksum combination.

#### Primary key
data_non_folio_rfnd_item_id

#### Tags
    - object_name=non_folio_rfnd_itm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__non_folio_rfnd_itm_versioned %}

#### Object Name
non_folio_rfnd_itm_versioned

#### Object Definition
This table tracks refunds that occur at the Front Desk for items that would not be included in a guest folio.NON_FOLIO_RFND_ITEM_TYP_NM, Parking Refunds, Other Refunds, Machine Refunds

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_non_folio_rfnd_item_id & metadata_checksum combination.

#### Primary key
data_non_folio_rfnd_item_id

#### Tags
    - object_name=non_folio_rfnd_itm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}