{% docs sil__intermediate__dreams__accounting__ofst_pgrp_config_cleansed %}

#### Object Name
ofst_pgrp_config_cleansed

#### Object Definition
Configures the Post Groups, Revenue Class ID, Revenue Type Code, Product ID and PKG ID if applicable for the Offset accounts

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_ofst_pst_grp_config_id & metadata_checksum combination.

#### Primary key
data_ofst_pst_grp_config_id

#### Tags
    - object_name=ofst_pgrp_config
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__ofst_pgrp_config_versioned %}

#### Object Name
ofst_pgrp_config_versioned

#### Object Definition
Configures the Post Groups, Revenue Class ID, Revenue Type Code, Product ID and PKG ID if applicable for the Offset accounts

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_ofst_pst_grp_config_id & metadata_checksum combination.

#### Primary key
data_ofst_pst_grp_config_id

#### Tags
    - object_name=ofst_pgrp_config
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}