{% docs sil__intermediate__xbms__wdw__dsny_fac_band_invtry_cleansed %}

#### Object Name
dsny_fac_band_invtry_cleansed

#### Object Definition
Table for the facility band inventory and the mapping disney facility ID and experience band transaction ID.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_dsny_fac_band_invtry_id & metadata_checksum combination.

#### Primary key
data_dsny_fac_band_invtry_id

#### Tags
    - object_name=dsny_fac_band_invtry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__dsny_fac_band_invtry_versioned %}

#### Object Name
dsny_fac_band_invtry_versioned

#### Object Definition
Table for the facility band inventory and the mapping disney facility ID and experience band transaction ID.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_dsny_fac_band_invtry_id & metadata_checksum combination.

#### Primary key
data_dsny_fac_band_invtry_id

#### Tags
    - object_name=dsny_fac_band_invtry
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}