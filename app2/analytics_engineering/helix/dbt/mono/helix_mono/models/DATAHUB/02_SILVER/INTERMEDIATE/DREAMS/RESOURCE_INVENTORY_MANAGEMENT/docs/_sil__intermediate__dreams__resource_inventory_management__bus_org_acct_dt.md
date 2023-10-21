{% docs sil__intermediate__dreams__resource_inventory_management__bus_org_acct_dt_cleansed %}

#### Object Name
bus_org_acct_dt_cleansed

#### Object Definition
This table is updated by the Accounting Date Roll job by business organization

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_bus_org_id & metadata_checksum combination.

#### Primary key
data_bus_org_id

#### Tags
    - object_name=bus_org_acct_dt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__bus_org_acct_dt_versioned %}

#### Object Name
bus_org_acct_dt_versioned

#### Object Definition
This table is updated by the Accounting Date Roll job by business organization

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_bus_org_id & metadata_checksum combination.

#### Primary key
data_bus_org_id

#### Tags
    - object_name=bus_org_acct_dt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}