{% docs sil__intermediate__level__n_wdw__extnl_sys_enttl_cleansed %}

#### Object Name
extnl_sys_enttl_cleansed

#### Object Definition
Contains external system entitlement names and ID such as TDSSN, ATS Reservation ID of the Level N entitlement sent in by the external systems that talk to Level N.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_extnl_sys_lvl_n_enttl_id & metadata_checksum combination.

#### Primary key
data_extnl_sys_lvl_n_enttl_id

#### Tags
    - object_name=extnl_sys_enttl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__extnl_sys_enttl_versioned %}

#### Object Name
extnl_sys_enttl_versioned

#### Object Definition
Contains external system entitlement names and ID such as TDSSN, ATS Reservation ID of the Level N entitlement sent in by the external systems that talk to Level N.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_extnl_sys_lvl_n_enttl_id & metadata_checksum combination.

#### Primary key
data_extnl_sys_lvl_n_enttl_id

#### Tags
    - object_name=extnl_sys_enttl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}