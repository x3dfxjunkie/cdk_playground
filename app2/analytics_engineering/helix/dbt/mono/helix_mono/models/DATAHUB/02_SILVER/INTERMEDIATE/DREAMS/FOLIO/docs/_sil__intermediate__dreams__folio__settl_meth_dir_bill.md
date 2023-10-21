{% docs sil__intermediate__dreams__folio__settl_meth_dir_bill_cleansed %}

#### Object Name
settl_meth_dir_bill_cleansed

#### Object Definition
This table contains the settlement method that is to Directly Bill the guest/Organization

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_settl_meth_id & metadata_checksum combination.

#### Primary key
data_settl_meth_id

#### Tags
    - object_name=settl_meth_dir_bill
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__settl_meth_dir_bill_versioned %}

#### Object Name
settl_meth_dir_bill_versioned

#### Object Definition
This table contains the settlement method that is to Directly Bill the guest/Organization

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_settl_meth_id & metadata_checksum combination.

#### Primary key
data_settl_meth_id

#### Tags
    - object_name=settl_meth_dir_bill
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}