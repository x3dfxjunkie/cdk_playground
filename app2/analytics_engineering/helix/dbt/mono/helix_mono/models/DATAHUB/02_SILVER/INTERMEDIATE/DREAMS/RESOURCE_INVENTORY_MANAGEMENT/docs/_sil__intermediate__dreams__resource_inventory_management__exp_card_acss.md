{% docs sil__intermediate__dreams__resource_inventory_management__exp_card_acss_cleansed %}

#### Object Name
exp_card_acss_cleansed

#### Object Definition
This table associates a unique identifier for the various areas within a resort that are accessible to cast and guest

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_exprnc_card_accs_id & metadata_checksum combination.

#### Primary key
data_exprnc_card_accs_id

#### Tags
    - object_name=exp_card_acss
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__exp_card_acss_versioned %}

#### Object Name
exp_card_acss_versioned

#### Object Definition
This table associates a unique identifier for the various areas within a resort that are accessible to cast and guest

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_exprnc_card_accs_id & metadata_checksum combination.

#### Primary key
data_exprnc_card_accs_id

#### Tags
    - object_name=exp_card_acss
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}