{% docs sil__intermediate__xbms__wdw__dsny_fac_lnk_cleansed %}

#### Object Name
dsny_fac_lnk_cleansed

#### Object Definition
Mapping table that maps the relationship between a parent XBMS facility ID and a child XBMS facility ID.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_dsny_fac_lnk_id & metadata_checksum combination.

#### Primary key
data_dsny_fac_lnk_id

#### Tags
    - object_name=dsny_fac_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__dsny_fac_lnk_versioned %}

#### Object Name
dsny_fac_lnk_versioned

#### Object Definition
Mapping table that maps the relationship between a parent XBMS facility ID and a child XBMS facility ID.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_dsny_fac_lnk_id & metadata_checksum combination.

#### Primary key
data_dsny_fac_lnk_id

#### Tags
    - object_name=dsny_fac_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}