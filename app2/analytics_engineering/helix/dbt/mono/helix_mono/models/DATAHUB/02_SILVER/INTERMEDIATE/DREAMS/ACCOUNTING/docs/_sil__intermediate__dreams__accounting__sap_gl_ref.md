{% docs sil__intermediate__dreams__accounting__sap_gl_ref_cleansed %}

#### Object Name
sap_gl_ref_cleansed

#### Object Definition
SAP General Ledger References associated to a SAP General Ledger Reference IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_sap_gl_ref_id & metadata_checksum combination.

#### Primary key
data_sap_gl_ref_id

#### Tags
    - object_name=sap_gl_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__sap_gl_ref_versioned %}

#### Object Name
sap_gl_ref_versioned

#### Object Definition
SAP General Ledger References associated to a SAP General Ledger Reference IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_sap_gl_ref_id & metadata_checksum combination.

#### Primary key
data_sap_gl_ref_id

#### Tags
    - object_name=sap_gl_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}