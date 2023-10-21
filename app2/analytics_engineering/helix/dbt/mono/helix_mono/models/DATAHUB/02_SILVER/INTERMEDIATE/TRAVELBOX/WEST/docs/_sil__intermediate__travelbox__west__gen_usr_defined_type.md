{% docs sil__intermediate__travelbox__west__gen_usr_defined_type_cleansed %}

#### Object Name
gen_usr_defined_type_cleansed

#### Object Definition
User defined attribute types related to generic product bookings

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_contract_id, data_user_defined_type_id & metadata_checksum combination.

#### Primary key
data_contract_id, data_user_defined_type_id

#### Tags
    - object_name=gen_usr_defined_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__gen_usr_defined_type_versioned %}

#### Object Name
gen_usr_defined_type_versioned

#### Object Definition
User defined attribute types related to generic product bookings

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_contract_id, data_user_defined_type_id & metadata_checksum combination.

#### Primary key
data_contract_id, data_user_defined_type_id

#### Tags
    - object_name=gen_usr_defined_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}