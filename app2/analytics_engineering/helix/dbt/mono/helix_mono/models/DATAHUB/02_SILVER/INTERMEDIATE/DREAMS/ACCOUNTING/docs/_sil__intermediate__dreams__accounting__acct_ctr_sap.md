{% docs sil__intermediate__dreams__accounting__acct_ctr_sap_cleansed %}

#### Object Name
acct_ctr_sap_cleansed

#### Object Definition
Account Centers associated to relevant SAP fields

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acct_ctr_sap_id & metadata_checksum combination.

#### Primary key
data_acct_ctr_sap_id

#### Tags
    - object_name=acct_ctr_sap
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__acct_ctr_sap_versioned %}

#### Object Name
acct_ctr_sap_versioned

#### Object Definition
Account Centers associated to relevant SAP fields

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acct_ctr_sap_id & metadata_checksum combination.

#### Primary key
data_acct_ctr_sap_id

#### Tags
    - object_name=acct_ctr_sap
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}