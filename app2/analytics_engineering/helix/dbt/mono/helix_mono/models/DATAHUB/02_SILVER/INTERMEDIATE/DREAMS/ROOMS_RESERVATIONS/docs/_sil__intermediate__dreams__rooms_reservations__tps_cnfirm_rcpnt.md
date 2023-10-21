{% docs sil__intermediate__dreams__rooms_reservations__tps_cnfirm_rcpnt_cleansed %}

#### Object Name
tps_cnfirm_rcpnt_cleansed

#### Object Definition
This table holds the information about who gets the confirmation of the reservation and where it goes

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tps_cnfirm_rcpnt_id & metadata_checksum combination.

#### Primary key
data_tps_cnfirm_rcpnt_id

#### Tags
    - object_name=tps_cnfirm_rcpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tps_cnfirm_rcpnt_versioned %}

#### Object Name
tps_cnfirm_rcpnt_versioned

#### Object Definition
This table holds the information about who gets the confirmation of the reservation and where it goes

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tps_cnfirm_rcpnt_id & metadata_checksum combination.

#### Primary key
data_tps_cnfirm_rcpnt_id

#### Tags
    - object_name=tps_cnfirm_rcpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}