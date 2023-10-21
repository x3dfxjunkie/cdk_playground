{% docs sil__intermediate__travelbox__west__contract_group_cleansed %}

#### Object Name
contract_group_cleansed

#### Object Definition
This contains the contract group defined based on a unique REFERENCE. There can be one or more version(s) under different contract ID from the same contract group in the relavent product contract table ( e.g: ACC_CONTRACT, TRS_CONTRACT). User can set up a contract group from any product client (Accomadation Client, Transfer Client).

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_group_id & metadata_checksum combination.

#### Primary key
data_group_id

#### Tags
    - object_name=contract_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__contract_group_versioned %}

#### Object Name
contract_group_versioned

#### Object Definition
This contains the contract group defined based on a unique REFERENCE. There can be one or more version(s) under different contract ID from the same contract group in the relavent product contract table ( e.g: ACC_CONTRACT, TRS_CONTRACT). User can set up a contract group from any product client (Accomadation Client, Transfer Client).

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_group_id & metadata_checksum combination.

#### Primary key
data_group_id

#### Tags
    - object_name=contract_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}