{% docs sil__intermediate__dreams__folio__bank_dpst_cleansed %}

#### Object Name
bank_dpst_cleansed

#### Object Definition
This table provides information regarding a front desk cashier deposit at the end of their shift

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_bank_dpst_id & metadata_checksum combination.

#### Primary key
data_bank_dpst_id

#### Tags
    - object_name=bank_dpst
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__bank_dpst_versioned %}

#### Object Name
bank_dpst_versioned

#### Object Definition
This table provides information regarding a front desk cashier deposit at the end of their shift

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_bank_dpst_id & metadata_checksum combination.

#### Primary key
data_bank_dpst_id

#### Tags
    - object_name=bank_dpst
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}