{% docs sil__intermediate__dreams__rooms_fulfillment__grp_tc_grp_cleansed %}

#### Object Name
grp_tc_grp_cleansed

#### Object Definition
When a reservation is a part of a convention, wedding, sporting event, there is a Group/Block code that identifies the group and is used for blocking rooms and also for billing. This table holds that Group code and the Group Team ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_grp_nb & metadata_checksum combination.

#### Primary key
data_tc_grp_nb

#### Tags
    - object_name=grp_tc_grp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__grp_tc_grp_versioned %}

#### Object Name
grp_tc_grp_versioned

#### Object Definition
When a reservation is a part of a convention, wedding, sporting event, there is a Group/Block code that identifies the group and is used for blocking rooms and also for billing. This table holds that Group code and the Group Team ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_grp_nb & metadata_checksum combination.

#### Primary key
data_tc_grp_nb

#### Tags
    - object_name=grp_tc_grp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}