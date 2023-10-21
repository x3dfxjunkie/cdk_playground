{% docs sil__intermediate__dreams__rooms_reservations__pkg_tc_cleansed %}

#### Object Name
pkg_tc_cleansed

#### Object Definition
This table provides indicators for Resort Special Reservations, Room only and wholesale packages

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pkg_tc_id & metadata_checksum combination.

#### Primary key
data_pkg_tc_id

#### Tags
    - object_name=pkg_tc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__pkg_tc_versioned %}

#### Object Name
pkg_tc_versioned

#### Object Definition
This table provides indicators for Resort Special Reservations, Room only and wholesale packages

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pkg_tc_id & metadata_checksum combination.

#### Primary key
data_pkg_tc_id

#### Tags
    - object_name=pkg_tc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}