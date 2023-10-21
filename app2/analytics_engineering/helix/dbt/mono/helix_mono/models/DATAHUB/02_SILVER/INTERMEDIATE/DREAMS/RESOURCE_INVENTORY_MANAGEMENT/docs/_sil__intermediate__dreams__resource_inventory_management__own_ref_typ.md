{% docs sil__intermediate__dreams__resource_inventory_management__own_ref_typ_cleansed %}

#### Object Name
own_ref_typ_cleansed

#### Object Definition
List of owner reference types: OWN_REF_TYP_NM
FREEZE_ID
ORIGINAL_TC
TEAM_NM
SE_RSRC_NO
TC
TP
DPMS_RES_NUMBER
TPS
INVTRY_TRACKING_ID
INVENTORY_REQUEST
PARENT_ASGNT_OWN
DPMS_TC

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_own_ref_typ_nm & metadata_checksum combination.

#### Primary key
data_own_ref_typ_nm

#### Tags
    - object_name=own_ref_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__own_ref_typ_versioned %}

#### Object Name
own_ref_typ_versioned

#### Object Definition
List of owner reference types: OWN_REF_TYP_NM
FREEZE_ID
ORIGINAL_TC
TEAM_NM
SE_RSRC_NO
TC
TP
DPMS_RES_NUMBER
TPS
INVTRY_TRACKING_ID
INVENTORY_REQUEST
PARENT_ASGNT_OWN
DPMS_TC

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_own_ref_typ_nm & metadata_checksum combination.

#### Primary key
data_own_ref_typ_nm

#### Tags
    - object_name=own_ref_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}