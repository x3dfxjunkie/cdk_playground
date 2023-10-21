{% docs sil__intermediate__dreams__folio__tax_exmpt_typ_cleansed %}

#### Object Name
tax_exmpt_typ_cleansed

#### Object Definition
Domain table for the types of organizations that are exempt from paying tax

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tax_exmpt_typ_nm & metadata_checksum combination.

#### Primary key
data_tax_exmpt_typ_nm

#### Tags
    - object_name=tax_exmpt_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__tax_exmpt_typ_versioned %}

#### Object Name
tax_exmpt_typ_versioned

#### Object Definition
Domain table for the types of organizations that are exempt from paying tax

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tax_exmpt_typ_nm & metadata_checksum combination.

#### Primary key
data_tax_exmpt_typ_nm

#### Tags
    - object_name=tax_exmpt_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}