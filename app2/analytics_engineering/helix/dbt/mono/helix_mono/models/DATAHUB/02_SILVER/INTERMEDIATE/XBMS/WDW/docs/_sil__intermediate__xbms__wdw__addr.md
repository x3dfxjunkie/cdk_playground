{% docs sil__intermediate__xbms__wdw__addr_cleansed %}

#### Object Name
addr_cleansed

#### Object Definition
Contains addresses for xband recipients.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_addr_id & metadata_checksum combination.

#### Primary key
data_addr_id

#### Tags
    - object_name=addr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__addr_versioned %}

#### Object Name
addr_versioned

#### Object Definition
Contains addresses for xband recipients.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_addr_id & metadata_checksum combination.

#### Primary key
data_addr_id

#### Tags
    - object_name=addr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}