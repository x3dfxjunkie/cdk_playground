{% docs sil__intermediate__level__n_wdw__lvl_n_lnk_rl_cleansed %}

#### Object Name
lvl_n_lnk_rl_cleansed

#### Object Definition
Describes the various roles for individuals that are participating in a transaction. A party may perform multiple roles. Roles are shared by multiple people. The same party could be a guest, mother of the bride, group contact, DVC owner and shareholder and more. For Memory Maker, examples are Participant, Non Participant

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_lnk_id, data_lvl_n_rl_id & metadata_checksum combination.

#### Primary key
data_lvl_n_lnk_id, data_lvl_n_rl_id

#### Tags
    - object_name=lvl_n_lnk_rl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_lnk_rl_versioned %}

#### Object Name
lvl_n_lnk_rl_versioned

#### Object Definition
Describes the various roles for individuals that are participating in a transaction. A party may perform multiple roles. Roles are shared by multiple people. The same party could be a guest, mother of the bride, group contact, DVC owner and shareholder and more. For Memory Maker, examples are Participant, Non Participant

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_lnk_id, data_lvl_n_rl_id & metadata_checksum combination.

#### Primary key
data_lvl_n_lnk_id, data_lvl_n_rl_id

#### Tags
    - object_name=lvl_n_lnk_rl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}