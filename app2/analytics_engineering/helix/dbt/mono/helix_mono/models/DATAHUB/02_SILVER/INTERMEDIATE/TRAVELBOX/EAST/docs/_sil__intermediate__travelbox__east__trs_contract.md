{% docs sil__intermediate__travelbox__east__trs_contract_cleansed %}

#### Object Name
trs_contract_cleansed

#### Object Definition
store Transfer and Excursion contract related basic data, this table will populate when we add the transfer or excursion item to the transfer contract

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_contract_id & metadata_checksum combination.

#### Primary key
data_contract_id

#### Tags
    - object_name=trs_contract
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__trs_contract_versioned %}

#### Object Name
trs_contract_versioned

#### Object Definition
store Transfer and Excursion contract related basic data, this table will populate when we add the transfer or excursion item to the transfer contract

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_contract_id & metadata_checksum combination.

#### Primary key
data_contract_id

#### Tags
    - object_name=trs_contract
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}