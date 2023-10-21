{% docs sil__intermediate__dreams__accounting__sap_cost_ctr_cleansed %}

#### Object Name
sap_cost_ctr_cleansed

#### Object Definition
SAP Cost Center names associated to SAP Cost Center Codes

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_sap_cost_ctr_cd & metadata_checksum combination.

#### Primary key
data_sap_cost_ctr_cd

#### Tags
    - object_name=sap_cost_ctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__sap_cost_ctr_versioned %}

#### Object Name
sap_cost_ctr_versioned

#### Object Definition
SAP Cost Center names associated to SAP Cost Center Codes

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_sap_cost_ctr_cd & metadata_checksum combination.

#### Primary key
data_sap_cost_ctr_cd

#### Tags
    - object_name=sap_cost_ctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}