{% docs sil__intermediate__dreams__resource_inventory_management__cmps_bus_org_cleansed %}

#### Object Name
cmps_bus_org_cleansed

#### Object Definition
This table ties the campus locations to different business organizations:BUS_ORG_NM
WDW SE
WDW Resort Ops
WDW DRC
Pacific Region SE
Pacific Region Resort Ops
Pacific Region DRC
DLR SE
DLR Resort Ops
DLR DRC

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_bus_org_id & metadata_checksum combination.

#### Primary key
data_bus_org_id

#### Tags
    - object_name=cmps_bus_org
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__cmps_bus_org_versioned %}

#### Object Name
cmps_bus_org_versioned

#### Object Definition
This table ties the campus locations to different business organizations:BUS_ORG_NM
WDW SE
WDW Resort Ops
WDW DRC
Pacific Region SE
Pacific Region Resort Ops
Pacific Region DRC
DLR SE
DLR Resort Ops
DLR DRC

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_bus_org_id & metadata_checksum combination.

#### Primary key
data_bus_org_id

#### Tags
    - object_name=cmps_bus_org
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}