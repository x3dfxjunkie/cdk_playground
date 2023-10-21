{% docs sil__intermediate__dreams__resource_inventory_management__cmps_fac_cleansed %}

#### Object Name
cmps_fac_cleansed

#### Object Definition
This table associates a facility ID to its respective campus

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cmps_id, data_fac_id & metadata_checksum combination.

#### Primary key
data_cmps_id, data_fac_id

#### Tags
    - object_name=cmps_fac
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__cmps_fac_versioned %}

#### Object Name
cmps_fac_versioned

#### Object Definition
This table associates a facility ID to its respective campus

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cmps_id, data_fac_id & metadata_checksum combination.

#### Primary key
data_cmps_id, data_fac_id

#### Tags
    - object_name=cmps_fac
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}