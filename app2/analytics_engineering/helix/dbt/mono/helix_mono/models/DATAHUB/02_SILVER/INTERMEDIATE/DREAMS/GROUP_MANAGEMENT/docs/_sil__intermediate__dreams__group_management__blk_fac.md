{% docs sil__intermediate__dreams__group_management__blk_fac_cleansed %}

#### Object Name
blk_fac_cleansed

#### Object Definition
When a group/convention plans a visit to WDW and they plan on staying at a resort a Block of rooms is set aside for them, this table provides the facility ID associated to the Block code and the sequence of use if more than 1 facility is associated

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_blk_cd, data_fac_id & metadata_checksum combination.

#### Primary key
data_blk_cd, data_fac_id

#### Tags
    - object_name=blk_fac
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__group_management__blk_fac_versioned %}

#### Object Name
blk_fac_versioned

#### Object Definition
When a group/convention plans a visit to WDW and they plan on staying at a resort a Block of rooms is set aside for them, this table provides the facility ID associated to the Block code and the sequence of use if more than 1 facility is associated

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_blk_cd, data_fac_id & metadata_checksum combination.

#### Primary key
data_blk_cd, data_fac_id

#### Tags
    - object_name=blk_fac
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}