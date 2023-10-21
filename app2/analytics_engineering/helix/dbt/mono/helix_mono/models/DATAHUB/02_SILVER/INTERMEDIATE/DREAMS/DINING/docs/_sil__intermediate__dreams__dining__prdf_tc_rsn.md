{% docs sil__intermediate__dreams__dining__prdf_tc_rsn_cleansed %}

#### Object Name
prdf_tc_rsn_cleansed

#### Object Definition
If something was updated in a Travel Component, this table provides the types of of reasons why the update occured.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_prdf_tc_rsn_id & metadata_checksum combination.

#### Primary key
data_prdf_tc_rsn_id

#### Tags
    - object_name=prdf_tc_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__prdf_tc_rsn_versioned %}

#### Object Name
prdf_tc_rsn_versioned

#### Object Definition
If something was updated in a Travel Component, this table provides the types of of reasons why the update occured.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_prdf_tc_rsn_id & metadata_checksum combination.

#### Primary key
data_prdf_tc_rsn_id

#### Tags
    - object_name=prdf_tc_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}