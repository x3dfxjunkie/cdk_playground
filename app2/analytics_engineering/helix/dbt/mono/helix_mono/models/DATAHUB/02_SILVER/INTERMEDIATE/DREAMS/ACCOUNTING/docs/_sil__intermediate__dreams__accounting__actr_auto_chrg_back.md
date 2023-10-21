{% docs sil__intermediate__dreams__accounting__actr_auto_chrg_back_cleansed %}

#### Object Name
actr_auto_chrg_back_cleansed

#### Object Definition
Lists the Account Centers that allows Automatic Charge Back

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_actr_auto_chrg_back_id & metadata_checksum combination.

#### Primary key
data_actr_auto_chrg_back_id

#### Tags
    - object_name=actr_auto_chrg_back
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__actr_auto_chrg_back_versioned %}

#### Object Name
actr_auto_chrg_back_versioned

#### Object Definition
Lists the Account Centers that allows Automatic Charge Back

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_actr_auto_chrg_back_id & metadata_checksum combination.

#### Primary key
data_actr_auto_chrg_back_id

#### Tags
    - object_name=actr_auto_chrg_back
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}