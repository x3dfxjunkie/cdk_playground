{% docs sil__intermediate__dreams__accounting__sap_acct_cleansed %}

#### Object Name
sap_acct_cleansed

#### Object Definition
SAP General Ledger Account names associated to SAP General Ledger Account Numbers

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_sap_gl_acct_nb & metadata_checksum combination.

#### Primary key
data_sap_gl_acct_nb

#### Tags
    - object_name=sap_acct
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__sap_acct_versioned %}

#### Object Name
sap_acct_versioned

#### Object Definition
SAP General Ledger Account names associated to SAP General Ledger Account Numbers

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_sap_gl_acct_nb & metadata_checksum combination.

#### Primary key
data_sap_gl_acct_nb

#### Tags
    - object_name=sap_acct
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}