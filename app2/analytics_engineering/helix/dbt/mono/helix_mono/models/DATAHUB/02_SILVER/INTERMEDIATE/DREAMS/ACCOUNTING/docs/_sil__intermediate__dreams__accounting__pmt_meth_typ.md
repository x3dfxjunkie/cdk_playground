{% docs sil__intermediate__dreams__accounting__pmt_meth_typ_cleansed %}

#### Object Name
pmt_meth_typ_cleansed

#### Object Definition
List of payment method types and the codes associated to them

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pmt_meth_typ_nm & metadata_checksum combination.

#### Primary key
data_pmt_meth_typ_nm

#### Tags
    - object_name=pmt_meth_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__pmt_meth_typ_versioned %}

#### Object Name
pmt_meth_typ_versioned

#### Object Definition
List of payment method types and the codes associated to them

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pmt_meth_typ_nm & metadata_checksum combination.

#### Primary key
data_pmt_meth_typ_nm

#### Tags
    - object_name=pmt_meth_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}