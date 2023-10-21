{% docs sil__intermediate__dreams__accounting__chrg_cd_infc_pmth_cleansed %}

#### Object Name
chrg_cd_infc_pmth_cleansed

#### Object Definition
Configuration of SAP IDs that are associated to a payment method

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrg_cd_infc_pmt_meth_id & metadata_checksum combination.

#### Primary key
data_chrg_cd_infc_pmt_meth_id

#### Tags
    - object_name=chrg_cd_infc_pmth
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__chrg_cd_infc_pmth_versioned %}

#### Object Name
chrg_cd_infc_pmth_versioned

#### Object Definition
Configuration of SAP IDs that are associated to a payment method

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrg_cd_infc_pmt_meth_id & metadata_checksum combination.

#### Primary key
data_chrg_cd_infc_pmt_meth_id

#### Tags
    - object_name=chrg_cd_infc_pmth
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}