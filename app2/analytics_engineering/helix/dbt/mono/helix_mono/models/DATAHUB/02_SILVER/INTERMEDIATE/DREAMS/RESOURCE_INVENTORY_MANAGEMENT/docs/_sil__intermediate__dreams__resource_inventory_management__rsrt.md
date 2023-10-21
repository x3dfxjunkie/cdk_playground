{% docs sil__intermediate__dreams__resource_inventory_management__rsrt_cleansed %}

#### Object Name
rsrt_cleansed

#### Object Definition
List of Resort (Enterprise) Facility IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrt_fac_id & metadata_checksum combination.

#### Primary key
data_rsrt_fac_id

#### Tags
    - object_name=rsrt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__rsrt_versioned %}

#### Object Name
rsrt_versioned

#### Object Definition
List of Resort (Enterprise) Facility IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrt_fac_id & metadata_checksum combination.

#### Primary key
data_rsrt_fac_id

#### Tags
    - object_name=rsrt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}