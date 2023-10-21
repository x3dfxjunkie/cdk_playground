{% docs sil__intermediate__dreams__accounting__strts_card_cls_cleansed %}

#### Object Name
strts_card_cls_cleansed

#### Object Definition
Stratus Card Class names associated to Stratus Card Class IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_strts_card_cls_cd & metadata_checksum combination.

#### Primary key
data_strts_card_cls_cd

#### Tags
    - object_name=strts_card_cls
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__strts_card_cls_versioned %}

#### Object Name
strts_card_cls_versioned

#### Object Definition
Stratus Card Class names associated to Stratus Card Class IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_strts_card_cls_cd & metadata_checksum combination.

#### Primary key
data_strts_card_cls_cd

#### Tags
    - object_name=strts_card_cls
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}