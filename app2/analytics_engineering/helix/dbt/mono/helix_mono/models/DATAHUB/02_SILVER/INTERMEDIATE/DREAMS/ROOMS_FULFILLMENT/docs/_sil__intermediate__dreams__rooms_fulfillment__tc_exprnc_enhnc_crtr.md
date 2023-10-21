{% docs sil__intermediate__dreams__rooms_fulfillment__tc_exprnc_enhnc_crtr_cleansed %}

#### Object Name
tc_exprnc_enhnc_crtr_cleansed

#### Object Definition
Criteria required to be able to experience the enhancement

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_elig_crtr_nm & metadata_checksum combination.

#### Primary key
data_elig_crtr_nm

#### Tags
    - object_name=tc_exprnc_enhnc_crtr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__tc_exprnc_enhnc_crtr_versioned %}

#### Object Name
tc_exprnc_enhnc_crtr_versioned

#### Object Definition
Criteria required to be able to experience the enhancement

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_elig_crtr_nm & metadata_checksum combination.

#### Primary key
data_elig_crtr_nm

#### Tags
    - object_name=tc_exprnc_enhnc_crtr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}