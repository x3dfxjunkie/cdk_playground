{% docs sil__intermediate__dreams__accounting__rev_cls_cleansed %}

#### Object Name
rev_cls_cleansed

#### Object Definition
List of Revenue Class names associated to Revenue Class IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rev_cls_id & metadata_checksum combination.

#### Primary key
data_rev_cls_id

#### Tags
    - object_name=rev_cls
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__rev_cls_versioned %}

#### Object Name
rev_cls_versioned

#### Object Definition
List of Revenue Class names associated to Revenue Class IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rev_cls_id & metadata_checksum combination.

#### Primary key
data_rev_cls_id

#### Tags
    - object_name=rev_cls
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}