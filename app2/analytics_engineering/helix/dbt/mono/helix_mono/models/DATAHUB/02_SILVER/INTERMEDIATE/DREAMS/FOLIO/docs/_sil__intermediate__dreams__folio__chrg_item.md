{% docs sil__intermediate__dreams__folio__chrg_item_cleansed %}

#### Object Name
chrg_item_cleansed

#### Object Definition
This table has the items associated to certain charges, there are 2 types: CHRG_ITEM_TYP_NM (Additional, Base) This are associated to 45 different revenue types, the main ones being BASE, DISCOUNT and different state/county taxes

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrg_item_id & metadata_checksum combination.

#### Primary key
data_chrg_item_id

#### Tags
    - object_name=chrg_item
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__chrg_item_versioned %}

#### Object Name
chrg_item_versioned

#### Object Definition
This table has the items associated to certain charges, there are 2 types: CHRG_ITEM_TYP_NM (Additional, Base) This are associated to 45 different revenue types, the main ones being BASE, DISCOUNT and different state/county taxes

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrg_item_id & metadata_checksum combination.

#### Primary key
data_chrg_item_id

#### Tags
    - object_name=chrg_item
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}