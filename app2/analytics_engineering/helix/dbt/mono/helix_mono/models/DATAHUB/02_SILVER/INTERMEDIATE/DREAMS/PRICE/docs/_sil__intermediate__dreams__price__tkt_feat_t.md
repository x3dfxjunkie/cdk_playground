{% docs sil__intermediate__dreams__price__tkt_feat_t_cleansed %}

#### Object Name
tkt_feat_t_cleansed

#### Object Definition
Features of a Ticket

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_feat_id, data_tkt_id & metadata_checksum combination.

#### Primary key
data_feat_id, data_tkt_id

#### Tags
    - object_name=tkt_feat_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__tkt_feat_t_versioned %}

#### Object Name
tkt_feat_t_versioned

#### Object Definition
Features of a Ticket

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_feat_id, data_tkt_id & metadata_checksum combination.

#### Primary key
data_feat_id, data_tkt_id

#### Tags
    - object_name=tkt_feat_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}