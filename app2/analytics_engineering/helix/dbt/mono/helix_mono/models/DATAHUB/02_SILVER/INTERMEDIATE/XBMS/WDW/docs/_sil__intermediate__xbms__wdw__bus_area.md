{% docs sil__intermediate__xbms__wdw__bus_area_cleansed %}

#### Object Name
bus_area_cleansed

#### Object Definition
Reference table for the business area ID and their code and description. Such as WDPR or DCL.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_bus_area_id & metadata_checksum combination.

#### Primary key
data_bus_area_id

#### Tags
    - object_name=bus_area
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__bus_area_versioned %}

#### Object Name
bus_area_versioned

#### Object Definition
Reference table for the business area ID and their code and description. Such as WDPR or DCL.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_bus_area_id & metadata_checksum combination.

#### Primary key
data_bus_area_id

#### Tags
    - object_name=bus_area
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}