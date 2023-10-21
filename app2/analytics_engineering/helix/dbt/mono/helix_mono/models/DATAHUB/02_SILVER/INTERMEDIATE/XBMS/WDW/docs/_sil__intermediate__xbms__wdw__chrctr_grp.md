{% docs sil__intermediate__xbms__wdw__chrctr_grp_cleansed %}

#### Object Name
chrctr_grp_cleansed

#### Object Definition
Reference table for brand types and their character groups such as Marvel, DVC, Princess, Run Disney, Polynesian Village, etc.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrctr_cd & metadata_checksum combination.

#### Primary key
data_chrctr_cd

#### Tags
    - object_name=chrctr_grp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__chrctr_grp_versioned %}

#### Object Name
chrctr_grp_versioned

#### Object Definition
Reference table for brand types and their character groups such as Marvel, DVC, Princess, Run Disney, Polynesian Village, etc.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrctr_cd & metadata_checksum combination.

#### Primary key
data_chrctr_cd

#### Tags
    - object_name=chrctr_grp
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}