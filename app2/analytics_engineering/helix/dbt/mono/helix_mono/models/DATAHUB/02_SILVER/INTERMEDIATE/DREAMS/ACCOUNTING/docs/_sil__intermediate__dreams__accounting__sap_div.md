{% docs sil__intermediate__dreams__accounting__sap_div_cleansed %}

#### Object Name
sap_div_cleansed

#### Object Definition
SAP Division names associated to SAP Division Code

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_sap_div_cd & metadata_checksum combination.

#### Primary key
data_sap_div_cd

#### Tags
    - object_name=sap_div
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__sap_div_versioned %}

#### Object Name
sap_div_versioned

#### Object Definition
SAP Division names associated to SAP Division Code

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_sap_div_cd & metadata_checksum combination.

#### Primary key
data_sap_div_cd

#### Tags
    - object_name=sap_div
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}