{% docs sil__intermediate__dreams__resource_inventory_management__rm_seq_cleansed %}

#### Object Name
rm_seq_cleansed

#### Object Definition
Room sequence IDs associated to reservable resource IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrc_id, data_rsrt_seq_id & metadata_checksum combination.

#### Primary key
data_rsrc_id, data_rsrt_seq_id

#### Tags
    - object_name=rm_seq
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rm_seq_versioned %}

#### Object Name
rm_seq_versioned

#### Object Definition
Room sequence IDs associated to reservable resource IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrc_id, data_rsrt_seq_id & metadata_checksum combination.

#### Primary key
data_rsrc_id, data_rsrt_seq_id

#### Tags
    - object_name=rm_seq
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}