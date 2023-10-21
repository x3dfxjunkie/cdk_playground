{% docs sil__intermediate__level__n_wdw__extnl_sys_cleansed %}

#### Object Name
extnl_sys_cleansed

#### Object Definition
Reference table for system identifiers external the source system, and their respective system names (ATS, DREAMS, One Source, Accovia).  These systems interact with the memory maker so

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_extnl_sys_id & metadata_checksum combination.

#### Primary key
data_extnl_sys_id

#### Tags
    - object_name=extnl_sys
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__extnl_sys_versioned %}

#### Object Name
extnl_sys_versioned

#### Object Definition
Reference table for system identifiers external the source system, and their respective system names (ATS, DREAMS, One Source, Accovia).  These systems interact with the memory maker so

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_extnl_sys_id & metadata_checksum combination.

#### Primary key
data_extnl_sys_id

#### Tags
    - object_name=extnl_sys
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}