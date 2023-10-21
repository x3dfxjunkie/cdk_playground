{% docs sil__intermediate__dreams__accounting__natr_pitm_config_cleansed %}

#### Object Name
natr_pitm_config_cleansed

#### Object Definition
Configures the Post Items, Source Account Center ID and Folio type for the Natural accounts

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_natr_pst_item_config_id & metadata_checksum combination.

#### Primary key
data_natr_pst_item_config_id

#### Tags
    - object_name=natr_pitm_config
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__natr_pitm_config_versioned %}

#### Object Name
natr_pitm_config_versioned

#### Object Definition
Configures the Post Items, Source Account Center ID and Folio type for the Natural accounts

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_natr_pst_item_config_id & metadata_checksum combination.

#### Primary key
data_natr_pst_item_config_id

#### Tags
    - object_name=natr_pitm_config
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}