{% docs sil__intermediate__xbms__wdw__cntry_cleansed %}

#### Object Name
cntry_cleansed

#### Object Definition
Reference table for the Country ID and the two letter and three letter (ISO 3166) country code and the written out country name.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cntry_id & metadata_checksum combination.

#### Primary key
data_cntry_id

#### Tags
    - object_name=cntry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__cntry_versioned %}

#### Object Name
cntry_versioned

#### Object Definition
Reference table for the Country ID and the two letter and three letter (ISO 3166) country code and the written out country name.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cntry_id & metadata_checksum combination.

#### Primary key
data_cntry_id

#### Tags
    - object_name=cntry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}