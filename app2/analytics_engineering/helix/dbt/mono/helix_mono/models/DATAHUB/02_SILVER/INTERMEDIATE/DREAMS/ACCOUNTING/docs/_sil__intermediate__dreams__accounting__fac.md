{% docs sil__intermediate__dreams__accounting__fac_cleansed %}

#### Object Name
fac_cleansed

#### Object Definition
Facilities tied to SAP and CAMPUS

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_fac_id & metadata_checksum combination.

#### Primary key
data_fac_id

#### Tags
    - object_name=fac
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__fac_versioned %}

#### Object Name
fac_versioned

#### Object Definition
Facilities tied to SAP and CAMPUS

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_fac_id & metadata_checksum combination.

#### Primary key
data_fac_id

#### Tags
    - object_name=fac
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}