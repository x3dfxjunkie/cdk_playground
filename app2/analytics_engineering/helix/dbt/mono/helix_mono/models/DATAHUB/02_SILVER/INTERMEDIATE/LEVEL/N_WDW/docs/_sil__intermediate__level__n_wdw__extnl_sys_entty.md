{% docs sil__intermediate__level__n_wdw__extnl_sys_entty_cleansed %}

#### Object Name
extnl_sys_entty_cleansed

#### Object Definition
Reference table of the external system entity names and their descriptions. such as titus-order-id, xid, xbms-link-id, barCodeNumber, etc.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_extnl_sys_entty_nm & metadata_checksum combination.

#### Primary key
data_extnl_sys_entty_nm

#### Tags
    - object_name=extnl_sys_entty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__extnl_sys_entty_versioned %}

#### Object Name
extnl_sys_entty_versioned

#### Object Definition
Reference table of the external system entity names and their descriptions. such as titus-order-id, xid, xbms-link-id, barCodeNumber, etc.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_extnl_sys_entty_nm & metadata_checksum combination.

#### Primary key
data_extnl_sys_entty_nm

#### Tags
    - object_name=extnl_sys_entty
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}