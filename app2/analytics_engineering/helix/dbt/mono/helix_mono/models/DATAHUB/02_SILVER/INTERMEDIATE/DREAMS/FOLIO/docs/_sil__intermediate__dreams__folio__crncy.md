{% docs sil__intermediate__dreams__folio__crncy_cleansed %}

#### Object Name
crncy_cleansed

#### Object Definition
Type of currency

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_crncy_iso_cd & metadata_checksum combination.

#### Primary key
data_crncy_iso_cd

#### Tags
    - object_name=crncy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__crncy_versioned %}

#### Object Name
crncy_versioned

#### Object Definition
Type of currency

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_crncy_iso_cd & metadata_checksum combination.

#### Primary key
data_crncy_iso_cd

#### Tags
    - object_name=crncy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}