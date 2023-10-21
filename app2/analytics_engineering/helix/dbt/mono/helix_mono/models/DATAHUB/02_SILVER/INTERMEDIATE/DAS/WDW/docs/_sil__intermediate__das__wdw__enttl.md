{% docs sil__intermediate__das__wdw__enttl_cleansed %}

#### Object Name
enttl_cleansed

#### Object Definition
Records attributes about the entitlement that is created when a Guest enrolls themselves and their party into the Disability Access Program such as the start and end dates, number of bookings allowed, and creation time.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_enttl_id & metadata_checksum combination.

#### Primary key
data_enttl_id

#### Tags
    - object_name=enttl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__das__wdw__enttl_versioned %}

#### Object Name
enttl_versioned

#### Object Definition
Records attributes about the entitlement that is created when a Guest enrolls themselves and their party into the Disability Access Program such as the start and end dates, number of bookings allowed, and creation time.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_enttl_id & metadata_checksum combination.

#### Primary key
data_enttl_id

#### Tags
    - object_name=enttl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}