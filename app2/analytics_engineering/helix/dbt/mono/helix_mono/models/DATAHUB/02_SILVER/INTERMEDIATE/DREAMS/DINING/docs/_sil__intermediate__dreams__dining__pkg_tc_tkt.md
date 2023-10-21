{% docs sil__intermediate__dreams__dining__pkg_tc_tkt_cleansed %}

#### Object Name
pkg_tc_tkt_cleansed

#### Object Definition
If a package on a reservation includes tickets, this table provides the date and time when the ticket was picked up and whether or not it was re-printed.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pkg_tc_id & metadata_checksum combination.

#### Primary key
data_pkg_tc_id

#### Tags
    - object_name=pkg_tc_tkt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__pkg_tc_tkt_versioned %}

#### Object Name
pkg_tc_tkt_versioned

#### Object Definition
If a package on a reservation includes tickets, this table provides the date and time when the ticket was picked up and whether or not it was re-printed.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pkg_tc_id & metadata_checksum combination.

#### Primary key
data_pkg_tc_id

#### Tags
    - object_name=pkg_tc_tkt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}