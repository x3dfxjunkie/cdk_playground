{% docs sil__intermediate__dreams__profile__srvc_cleansed %}

#### Object Name
srvc_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_srvc_id & metadata_checksum combination.

#### Primary key
data_srvc_id

#### Tags
    - object_name=srvc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__profile__srvc_versioned %}

#### Object Name
srvc_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_srvc_id & metadata_checksum combination.

#### Primary key
data_srvc_id

#### Tags
    - object_name=srvc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}