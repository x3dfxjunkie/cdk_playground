{% docs sil__intermediate__travelbox__west__acc_contract_cleansed %}

#### Object Name
acc_contract_cleansed

#### Object Definition
This table is used to store Accommodaion contract information. The values are setup in root node in Accommodation Manager

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_contract_id & metadata_checksum combination.

#### Primary key
data_contract_id

#### Tags
    - object_name=acc_contract
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__acc_contract_versioned %}

#### Object Name
acc_contract_versioned

#### Object Definition
This table is used to store Accommodaion contract information. The values are setup in root node in Accommodation Manager

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_contract_id & metadata_checksum combination.

#### Primary key
data_contract_id

#### Tags
    - object_name=acc_contract
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}