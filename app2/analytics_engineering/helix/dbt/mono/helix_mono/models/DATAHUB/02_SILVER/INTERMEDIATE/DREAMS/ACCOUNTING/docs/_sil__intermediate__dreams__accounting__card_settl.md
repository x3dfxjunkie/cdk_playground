{% docs sil__intermediate__dreams__accounting__card_settl_cleansed %}

#### Object Name
card_settl_cleansed

#### Object Definition
Provides all the information related to the Settlement method (guest putting a credit card on their reservations for incidentals

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_card_settl_id & metadata_checksum combination.

#### Primary key
data_card_settl_id

#### Tags
    - object_name=card_settl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__card_settl_versioned %}

#### Object Name
card_settl_versioned

#### Object Definition
Provides all the information related to the Settlement method (guest putting a credit card on their reservations for incidentals

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_card_settl_id & metadata_checksum combination.

#### Primary key
data_card_settl_id

#### Tags
    - object_name=card_settl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}