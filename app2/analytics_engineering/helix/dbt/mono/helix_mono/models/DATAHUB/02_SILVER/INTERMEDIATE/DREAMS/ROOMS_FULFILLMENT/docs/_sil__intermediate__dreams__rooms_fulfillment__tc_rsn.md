{% docs sil__intermediate__dreams__rooms_fulfillment__tc_rsn_cleansed %}

#### Object Name
tc_rsn_cleansed

#### Object Definition
This table provides the reason for certain actions associated to a travel component. It also has the FK for the Preferred Travel Component Reason

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_rsn_id & metadata_checksum combination.

#### Primary key
data_tc_rsn_id

#### Tags
    - object_name=tc_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__tc_rsn_versioned %}

#### Object Name
tc_rsn_versioned

#### Object Definition
This table provides the reason for certain actions associated to a travel component. It also has the FK for the Preferred Travel Component Reason

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_rsn_id & metadata_checksum combination.

#### Primary key
data_tc_rsn_id

#### Tags
    - object_name=tc_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}