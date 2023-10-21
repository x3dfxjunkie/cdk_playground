{% docs sil__intermediate__dreams__rooms_reservations__tc_grp_cleansed %}

#### Object Name
tc_grp_cleansed

#### Object Definition
This table ties together the reservation/package components and it also ties to the reservation information

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_grp_nb & metadata_checksum combination.

#### Primary key
data_tc_grp_nb

#### Tags
    - object_name=tc_grp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tc_grp_versioned %}

#### Object Name
tc_grp_versioned

#### Object Definition
This table ties together the reservation/package components and it also ties to the reservation information

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_grp_nb & metadata_checksum combination.

#### Primary key
data_tc_grp_nb

#### Tags
    - object_name=tc_grp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}