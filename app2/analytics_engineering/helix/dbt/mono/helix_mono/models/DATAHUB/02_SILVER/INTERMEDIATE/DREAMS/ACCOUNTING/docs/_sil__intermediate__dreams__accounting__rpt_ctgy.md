{% docs sil__intermediate__dreams__accounting__rpt_ctgy_cleansed %}

#### Object Name
rpt_ctgy_cleansed

#### Object Definition
Only one reporting category is still active this might be phased out

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rpt_ctgy_id & metadata_checksum combination.

#### Primary key
data_rpt_ctgy_id

#### Tags
    - object_name=rpt_ctgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__rpt_ctgy_versioned %}

#### Object Name
rpt_ctgy_versioned

#### Object Definition
Only one reporting category is still active this might be phased out

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rpt_ctgy_id & metadata_checksum combination.

#### Primary key
data_rpt_ctgy_id

#### Tags
    - object_name=rpt_ctgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}