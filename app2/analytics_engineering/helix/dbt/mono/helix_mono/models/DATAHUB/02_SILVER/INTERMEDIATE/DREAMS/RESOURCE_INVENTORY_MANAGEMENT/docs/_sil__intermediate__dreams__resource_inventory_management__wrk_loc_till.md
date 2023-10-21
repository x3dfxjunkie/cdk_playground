{% docs sil__intermediate__dreams__resource_inventory_management__wrk_loc_till_cleansed %}

#### Object Name
wrk_loc_till_cleansed

#### Object Definition
Till and work location IDs associated to a till type
Frontline Service Advisor
Manager
Graveyard
Cashier

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_till_id & metadata_checksum combination.

#### Primary key
data_till_id

#### Tags
    - object_name=wrk_loc_till
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__wrk_loc_till_versioned %}

#### Object Name
wrk_loc_till_versioned

#### Object Definition
Till and work location IDs associated to a till type
Frontline Service Advisor
Manager
Graveyard
Cashier

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_till_id & metadata_checksum combination.

#### Primary key
data_till_id

#### Tags
    - object_name=wrk_loc_till
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}