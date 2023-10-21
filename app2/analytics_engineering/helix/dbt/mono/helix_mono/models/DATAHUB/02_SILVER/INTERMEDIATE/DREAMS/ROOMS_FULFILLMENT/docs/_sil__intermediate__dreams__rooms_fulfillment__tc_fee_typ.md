{% docs sil__intermediate__dreams__rooms_fulfillment__tc_fee_typ_cleansed %}

#### Object Name
tc_fee_typ_cleansed

#### Object Definition
Types of fees associated to certain component types.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_fee_typ_nm & metadata_checksum combination.

#### Primary key
data_tc_fee_typ_nm

#### Tags
    - object_name=tc_fee_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__tc_fee_typ_versioned %}

#### Object Name
tc_fee_typ_versioned

#### Object Definition
Types of fees associated to certain component types.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_fee_typ_nm & metadata_checksum combination.

#### Primary key
data_tc_fee_typ_nm

#### Tags
    - object_name=tc_fee_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}