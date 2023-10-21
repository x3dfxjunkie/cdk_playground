{% docs sil__intermediate__xbms__wdw__dsny_fac_cleansed %}

#### Object Name
dsny_fac_cleansed

#### Object Definition
Reference table for Disney facilities in XBMS and corresponding address, facility type, shipping contact, enterprise facility id, and facility name.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_dsny_fac_id & metadata_checksum combination.

#### Primary key
data_dsny_fac_id

#### Tags
    - object_name=dsny_fac
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__dsny_fac_versioned %}

#### Object Name
dsny_fac_versioned

#### Object Definition
Reference table for Disney facilities in XBMS and corresponding address, facility type, shipping contact, enterprise facility id, and facility name.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_dsny_fac_id & metadata_checksum combination.

#### Primary key
data_dsny_fac_id

#### Tags
    - object_name=dsny_fac
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}