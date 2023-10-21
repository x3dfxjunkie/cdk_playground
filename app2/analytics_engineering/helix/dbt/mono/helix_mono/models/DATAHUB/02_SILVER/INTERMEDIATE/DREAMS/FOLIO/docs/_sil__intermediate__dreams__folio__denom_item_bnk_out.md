{% docs sil__intermediate__dreams__folio__denom_item_bnk_out_cleansed %}

#### Object Name
denom_item_bnk_out_cleansed

#### Object Definition
This table connects the type of denomination that is included in a front desk cashier&#39;s till bank out: DENOM_ITEM_TYP_NM (DISNEY_DOLLAR, TRAVELERS_CHECK, CURRENCY, COIN)

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_denom_item_bnk_out_id & metadata_checksum combination.

#### Primary key
data_denom_item_bnk_out_id

#### Tags
    - object_name=denom_item_bnk_out
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__denom_item_bnk_out_versioned %}

#### Object Name
denom_item_bnk_out_versioned

#### Object Definition
This table connects the type of denomination that is included in a front desk cashier&#39;s till bank out: DENOM_ITEM_TYP_NM (DISNEY_DOLLAR, TRAVELERS_CHECK, CURRENCY, COIN)

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_denom_item_bnk_out_id & metadata_checksum combination.

#### Primary key
data_denom_item_bnk_out_id

#### Tags
    - object_name=denom_item_bnk_out
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}