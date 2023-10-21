{% docs sil__intermediate__dreams__dining__comnctn_chan_cleansed %}

#### Object Name
comnctn_chan_cleansed

#### Object Definition
Lookup table for how the reservation was entered into the system. Ie: Contact Center Unknown Direct Connect Internet Guest Facing GDS/External Channel Manager Travel Connect IVR

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_comnctn_chan_id & metadata_checksum combination.

#### Primary key
data_comnctn_chan_id

#### Tags
    - object_name=comnctn_chan
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__comnctn_chan_versioned %}

#### Object Name
comnctn_chan_versioned

#### Object Definition
Lookup table for how the reservation was entered into the system. Ie: Contact Center Unknown Direct Connect Internet Guest Facing GDS/External Channel Manager Travel Connect IVR

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_comnctn_chan_id & metadata_checksum combination.

#### Primary key
data_comnctn_chan_id

#### Tags
    - object_name=comnctn_chan
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}