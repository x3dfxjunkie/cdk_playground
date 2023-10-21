{% docs sil__intermediate__dreams__rooms_reservations__acm_cmpnt_cleansed %}

#### Object Name
acm_cmpnt_cleansed

#### Object Definition
This table contains only Accommodation components and it provides indicators for rooms with a Late Check Out, Special Need Request, or a room that have more than one reservation associated to that room, a sharewith.  This table also provides the Disney Vacation Club reservation type for each accommodation ie: Non Member Cash Member Points Member Non Discounted Cash Member Discounted Cash

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acm_tc_id & metadata_checksum combination.

#### Primary key
data_acm_tc_id

#### Tags
    - object_name=acm_cmpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__acm_cmpnt_versioned %}

#### Object Name
acm_cmpnt_versioned

#### Object Definition
This table contains only Accommodation components and it provides indicators for rooms with a Late Check Out, Special Need Request, or a room that have more than one reservation associated to that room, a sharewith.  This table also provides the Disney Vacation Club reservation type for each accommodation ie: Non Member Cash Member Points Member Non Discounted Cash Member Discounted Cash

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acm_tc_id & metadata_checksum combination.

#### Primary key
data_acm_tc_id

#### Tags
    - object_name=acm_cmpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}