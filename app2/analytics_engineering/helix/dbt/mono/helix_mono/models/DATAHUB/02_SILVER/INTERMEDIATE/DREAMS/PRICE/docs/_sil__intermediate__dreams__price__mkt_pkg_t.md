{% docs sil__intermediate__dreams__price__mkt_pkg_t_cleansed %}

#### Object Name
mkt_pkg_t_cleansed

#### Object Definition
This table provides additional information about the package including the Market Package Code which is how the package is marketed

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pkg_id & metadata_checksum combination.

#### Primary key
data_pkg_id

#### Tags
    - object_name=mkt_pkg_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__mkt_pkg_t_versioned %}

#### Object Name
mkt_pkg_t_versioned

#### Object Definition
This table provides additional information about the package including the Market Package Code which is how the package is marketed

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pkg_id & metadata_checksum combination.

#### Primary key
data_pkg_id

#### Tags
    - object_name=mkt_pkg_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}