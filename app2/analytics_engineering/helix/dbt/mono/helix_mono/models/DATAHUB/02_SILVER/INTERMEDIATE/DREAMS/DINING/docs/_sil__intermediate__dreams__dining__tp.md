{% docs sil__intermediate__dreams__dining__tp_cleansed %}

#### Object Name
tp_cleansed

#### Object Definition
This is the highest level of the guest Travel Plan, it ties together any room reservations or dining reservations associated to said Travel Plan. It includes the Travel Plan start and end dates

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tp_id & metadata_checksum combination.

#### Primary key
data_tp_id

#### Tags
    - object_name=tp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__tp_versioned %}

#### Object Name
tp_versioned

#### Object Definition
This is the highest level of the guest Travel Plan, it ties together any room reservations or dining reservations associated to said Travel Plan. It includes the Travel Plan start and end dates

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tp_id & metadata_checksum combination.

#### Primary key
data_tp_id

#### Tags
    - object_name=tp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}