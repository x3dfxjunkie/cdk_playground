{% docs sil__intermediate__dreams__folio__gbl_tkt_comm_cleansed %}

#### Object Name
gbl_tkt_comm_cleansed

#### Object Definition
This table ties the commission percentage for Tickets Last loaded on 1/26/2021

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_glbl_tkt_comm_id & metadata_checksum combination.

#### Primary key
data_glbl_tkt_comm_id

#### Tags
    - object_name=gbl_tkt_comm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__gbl_tkt_comm_versioned %}

#### Object Name
gbl_tkt_comm_versioned

#### Object Definition
This table ties the commission percentage for Tickets Last loaded on 1/26/2021

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_glbl_tkt_comm_id & metadata_checksum combination.

#### Primary key
data_glbl_tkt_comm_id

#### Tags
    - object_name=gbl_tkt_comm
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}