{% docs sil__intermediate__dreams__profile__prfl_typ_cleansed %}

#### Object Name
prfl_typ_cleansed

#### Object Definition
The list of profile types: Message; Service; GRAND_GATHERING_TYPE; Attribute; Comment; Alert

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_prfl_typ_nm & metadata_checksum combination.

#### Primary key
data_prfl_typ_nm

#### Tags
    - object_name=prfl_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__profile__prfl_typ_versioned %}

#### Object Name
prfl_typ_versioned

#### Object Definition
The list of profile types: Message; Service; GRAND_GATHERING_TYPE; Attribute; Comment; Alert

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_prfl_typ_nm & metadata_checksum combination.

#### Primary key
data_prfl_typ_nm

#### Tags
    - object_name=prfl_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}