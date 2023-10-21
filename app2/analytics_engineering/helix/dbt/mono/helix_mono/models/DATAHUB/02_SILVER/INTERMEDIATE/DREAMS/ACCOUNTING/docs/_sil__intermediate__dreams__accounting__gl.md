{% docs sil__intermediate__dreams__accounting__gl_cleansed %}

#### Object Name
gl_cleansed

#### Object Definition
Provides an account or record used to store bookkeeping entries for balance-sheet and income-statement transactions

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_gl_id & metadata_checksum combination.

#### Primary key
data_gl_id

#### Tags
    - object_name=gl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__gl_versioned %}

#### Object Name
gl_versioned

#### Object Definition
Provides an account or record used to store bookkeeping entries for balance-sheet and income-statement transactions

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_gl_id & metadata_checksum combination.

#### Primary key
data_gl_id

#### Tags
    - object_name=gl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}