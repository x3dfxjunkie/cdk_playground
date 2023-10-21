{% docs sil__intermediate__dreams__group_management__gro_cleansed %}

#### Object Name
gro_cleansed

#### Object Definition
This has the Group Office Name and Phone number

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_gro_nm & metadata_checksum combination.

#### Primary key
data_gro_nm

#### Tags
    - object_name=gro
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__gro_versioned %}

#### Object Name
gro_versioned

#### Object Definition
This has the Group Office Name and Phone number

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_gro_nm & metadata_checksum combination.

#### Primary key
data_gro_nm

#### Tags
    - object_name=gro
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}