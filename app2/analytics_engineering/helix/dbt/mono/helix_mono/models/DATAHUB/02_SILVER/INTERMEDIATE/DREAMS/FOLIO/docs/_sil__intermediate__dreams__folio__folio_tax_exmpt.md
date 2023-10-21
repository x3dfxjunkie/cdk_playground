{% docs sil__intermediate__dreams__folio__folio_tax_exmpt_cleansed %}

#### Object Name
folio_tax_exmpt_cleansed

#### Object Definition
This table ties the Tax Exempt ID to the Tax Exempt Certification number value

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tax_exmpt_id & metadata_checksum combination.

#### Primary key
data_tax_exmpt_id

#### Tags
    - object_name=folio_tax_exmpt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__folio_tax_exmpt_versioned %}

#### Object Name
folio_tax_exmpt_versioned

#### Object Definition
This table ties the Tax Exempt ID to the Tax Exempt Certification number value

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tax_exmpt_id & metadata_checksum combination.

#### Primary key
data_tax_exmpt_id

#### Tags
    - object_name=folio_tax_exmpt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}