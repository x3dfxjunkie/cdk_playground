{% docs sil__intermediate__dreams__resource_inventory_management__hskp_clng_sch_ovrd_cleansed %}

#### Object Name
hskp_clng_sch_ovrd_cleansed

#### Object Definition
This table indicates when a housekeeping schedule is overridden or not

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_hskp_clng_sch_ovrd_id & metadata_checksum combination.

#### Primary key
data_hskp_clng_sch_ovrd_id

#### Tags
    - object_name=hskp_clng_sch_ovrd
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__hskp_clng_sch_ovrd_versioned %}

#### Object Name
hskp_clng_sch_ovrd_versioned

#### Object Definition
This table indicates when a housekeeping schedule is overridden or not

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_hskp_clng_sch_ovrd_id & metadata_checksum combination.

#### Primary key
data_hskp_clng_sch_ovrd_id

#### Tags
    - object_name=hskp_clng_sch_ovrd
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}