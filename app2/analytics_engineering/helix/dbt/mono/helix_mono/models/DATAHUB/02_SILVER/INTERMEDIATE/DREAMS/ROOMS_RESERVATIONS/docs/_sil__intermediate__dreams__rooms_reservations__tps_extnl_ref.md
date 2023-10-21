{% docs sil__intermediate__dreams__rooms_reservations__tps_extnl_ref_cleansed %}

#### Object Name
tps_extnl_ref_cleansed

#### Object Definition
Reservation level travel plan segment records can have associated external references from various sources. External References are: (TPS_EXTNL_REF_TYP_NM, RESERVATION, ORIGINAL_TP_ID, MEMBERSHIP, LINKAGE, APP_REF)

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tps_extnl_ref_id & metadata_checksum combination.

#### Primary key
data_tps_extnl_ref_id

#### Tags
    - object_name=tps_extnl_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tps_extnl_ref_versioned %}

#### Object Name
tps_extnl_ref_versioned

#### Object Definition
Reservation level travel plan segment records can have associated external references from various sources. External References are: (TPS_EXTNL_REF_TYP_NM, RESERVATION, ORIGINAL_TP_ID, MEMBERSHIP, LINKAGE, APP_REF)

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tps_extnl_ref_id & metadata_checksum combination.

#### Primary key
data_tps_extnl_ref_id

#### Tags
    - object_name=tps_extnl_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}