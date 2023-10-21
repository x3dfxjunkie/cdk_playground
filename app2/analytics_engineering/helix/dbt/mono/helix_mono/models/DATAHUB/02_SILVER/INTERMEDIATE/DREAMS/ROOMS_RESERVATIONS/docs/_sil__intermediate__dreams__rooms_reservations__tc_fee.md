{% docs sil__intermediate__dreams__rooms_reservations__tc_fee_cleansed %}

#### Object Name
tc_fee_cleansed

#### Object Definition
There are fees associated to certain types of components that indicate that a fee was one of these types: Exchange Cancel

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_fee_id & metadata_checksum combination.

#### Primary key
data_tc_fee_id

#### Tags
    - object_name=tc_fee
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tc_fee_versioned %}

#### Object Name
tc_fee_versioned

#### Object Definition
There are fees associated to certain types of components that indicate that a fee was one of these types: Exchange Cancel

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_fee_id & metadata_checksum combination.

#### Primary key
data_tc_fee_id

#### Tags
    - object_name=tc_fee
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}