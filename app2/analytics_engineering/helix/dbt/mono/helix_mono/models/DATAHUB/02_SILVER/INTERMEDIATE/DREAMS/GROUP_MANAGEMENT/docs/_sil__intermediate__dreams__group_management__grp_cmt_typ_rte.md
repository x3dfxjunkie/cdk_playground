{% docs sil__intermediate__dreams__group_management__grp_cmt_typ_rte_cleansed %}

#### Object Name
grp_cmt_typ_rte_cleansed

#### Object Definition
Child table of Group Comment

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_grp_cmt_typ_rte_id & metadata_checksum combination.

#### Primary key
data_grp_cmt_typ_rte_id

#### Tags
    - object_name=grp_cmt_typ_rte
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__grp_cmt_typ_rte_versioned %}

#### Object Name
grp_cmt_typ_rte_versioned

#### Object Definition
Child table of Group Comment

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_grp_cmt_typ_rte_id & metadata_checksum combination.

#### Primary key
data_grp_cmt_typ_rte_id

#### Tags
    - object_name=grp_cmt_typ_rte
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}