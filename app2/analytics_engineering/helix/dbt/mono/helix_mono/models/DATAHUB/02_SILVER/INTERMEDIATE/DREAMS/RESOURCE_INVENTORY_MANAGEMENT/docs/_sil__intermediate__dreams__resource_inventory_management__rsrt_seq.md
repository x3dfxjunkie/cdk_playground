{% docs sil__intermediate__dreams__resource_inventory_management__rsrt_seq_cleansed %}

#### Object Name
rsrt_seq_cleansed

#### Object Definition
Resort Sequence IDs associated to Resort Facility IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrt_seq_id & metadata_checksum combination.

#### Primary key
data_rsrt_seq_id

#### Tags
    - object_name=rsrt_seq
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrt_seq_versioned %}

#### Object Name
rsrt_seq_versioned

#### Object Definition
Resort Sequence IDs associated to Resort Facility IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrt_seq_id & metadata_checksum combination.

#### Primary key
data_rsrt_seq_id

#### Tags
    - object_name=rsrt_seq
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}