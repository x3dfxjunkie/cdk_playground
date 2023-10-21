{% docs sil__intermediate__dreams__resource_inventory_management__wrk_loc_cleansed %}

#### Object Name
wrk_loc_cleansed

#### Object Definition
Work location IDs associated to resort facility IDs, Facility name, transactional account center ID, Bank account center ID and business organization ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_wrk_loc_id & metadata_checksum combination.

#### Primary key
data_wrk_loc_id

#### Tags
    - object_name=wrk_loc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__wrk_loc_versioned %}

#### Object Name
wrk_loc_versioned

#### Object Definition
Work location IDs associated to resort facility IDs, Facility name, transactional account center ID, Bank account center ID and business organization ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_wrk_loc_id & metadata_checksum combination.

#### Primary key
data_wrk_loc_id

#### Tags
    - object_name=wrk_loc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}