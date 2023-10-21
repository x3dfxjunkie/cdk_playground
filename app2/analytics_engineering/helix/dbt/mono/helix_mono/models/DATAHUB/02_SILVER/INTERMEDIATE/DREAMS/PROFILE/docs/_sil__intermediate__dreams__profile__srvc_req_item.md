{% docs sil__intermediate__dreams__profile__srvc_req_item_cleansed %}

#### Object Name
srvc_req_item_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_mxmo_item_nb, data_srvc_typ_nm & metadata_checksum combination.

#### Primary key
data_mxmo_item_nb, data_srvc_typ_nm

#### Tags
    - object_name=srvc_req_item
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__profile__srvc_req_item_versioned %}

#### Object Name
srvc_req_item_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_mxmo_item_nb, data_srvc_typ_nm & metadata_checksum combination.

#### Primary key
data_mxmo_item_nb, data_srvc_typ_nm

#### Tags
    - object_name=srvc_req_item
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}