{% docs sil__intermediate__travelbox__west__pkg_group_cleansed %}

#### Object Name
pkg_group_cleansed

#### Object Definition
Basic details of a package package code, package name are stored

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pkg_group_id & metadata_checksum combination.

#### Primary key
data_pkg_group_id

#### Tags
    - object_name=pkg_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__pkg_group_versioned %}

#### Object Name
pkg_group_versioned

#### Object Definition
Basic details of a package package code, package name are stored

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pkg_group_id & metadata_checksum combination.

#### Primary key
data_pkg_group_id

#### Tags
    - object_name=pkg_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}