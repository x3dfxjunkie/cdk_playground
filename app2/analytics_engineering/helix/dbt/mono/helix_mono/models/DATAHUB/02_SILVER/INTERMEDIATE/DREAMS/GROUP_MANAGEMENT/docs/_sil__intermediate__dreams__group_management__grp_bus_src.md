{% docs sil__intermediate__dreams__group_management__grp_bus_src_cleansed %}

#### Object Name
grp_bus_src_cleansed

#### Object Definition
Domain

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_grp_bus_src_nm & metadata_checksum combination.

#### Primary key
data_grp_bus_src_nm

#### Tags
    - object_name=grp_bus_src
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__grp_bus_src_versioned %}

#### Object Name
grp_bus_src_versioned

#### Object Definition
Domain

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_grp_bus_src_nm & metadata_checksum combination.

#### Primary key
data_grp_bus_src_nm

#### Tags
    - object_name=grp_bus_src
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}