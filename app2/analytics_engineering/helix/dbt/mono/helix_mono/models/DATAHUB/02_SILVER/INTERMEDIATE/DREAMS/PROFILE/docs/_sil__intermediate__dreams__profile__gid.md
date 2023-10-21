{% docs sil__intermediate__dreams__profile__gid_cleansed %}

#### Object Name
gid_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_gid_cls_nm & metadata_checksum combination.

#### Primary key
data_gid_cls_nm

#### Tags
    - object_name=gid
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__profile__gid_versioned %}

#### Object Name
gid_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_gid_cls_nm & metadata_checksum combination.

#### Primary key
data_gid_cls_nm

#### Tags
    - object_name=gid
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}