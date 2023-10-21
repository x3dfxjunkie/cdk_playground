{% docs sil__intermediate__dreams__accounting__rev_typ_cleansed %}

#### Object Name
rev_typ_cleansed

#### Object Definition
Revenue Type Names associated to Revenue Type IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rev_typ_id & metadata_checksum combination.

#### Primary key
data_rev_typ_id

#### Tags
    - object_name=rev_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__rev_typ_versioned %}

#### Object Name
rev_typ_versioned

#### Object Definition
Revenue Type Names associated to Revenue Type IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rev_typ_id & metadata_checksum combination.

#### Primary key
data_rev_typ_id

#### Tags
    - object_name=rev_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}