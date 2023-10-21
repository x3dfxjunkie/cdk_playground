{% docs sil__intermediate__level__n_wdw__tkt_void_typ_cleansed %}

#### Object Name
tkt_void_typ_cleansed

#### Object Definition
Reference table containing the ticket void type code and the description in Level N.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tkt_void_typ_cd & metadata_checksum combination.

#### Primary key
data_tkt_void_typ_cd

#### Tags
    - object_name=tkt_void_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__tkt_void_typ_versioned %}

#### Object Name
tkt_void_typ_versioned

#### Object Definition
Reference table containing the ticket void type code and the description in Level N.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tkt_void_typ_cd & metadata_checksum combination.

#### Primary key
data_tkt_void_typ_cd

#### Tags
    - object_name=tkt_void_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}