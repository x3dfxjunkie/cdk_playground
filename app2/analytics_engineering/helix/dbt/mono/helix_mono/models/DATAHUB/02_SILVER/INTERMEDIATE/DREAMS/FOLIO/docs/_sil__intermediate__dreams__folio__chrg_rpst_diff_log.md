{% docs sil__intermediate__dreams__folio__chrg_rpst_diff_log_cleansed %}

#### Object Name
chrg_rpst_diff_log_cleansed

#### Object Definition
This table holds the information related to a Repost, meaning that the interface between the reservation system and the POS system may not have connected properly and therefore, the charge is reposted and that is monitored by Fice

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrg_rpst_diff_log_id & metadata_checksum combination.

#### Primary key
data_chrg_rpst_diff_log_id

#### Tags
    - object_name=chrg_rpst_diff_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__chrg_rpst_diff_log_versioned %}

#### Object Name
chrg_rpst_diff_log_versioned

#### Object Definition
This table holds the information related to a Repost, meaning that the interface between the reservation system and the POS system may not have connected properly and therefore, the charge is reposted and that is monitored by Fice

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrg_rpst_diff_log_id & metadata_checksum combination.

#### Primary key
data_chrg_rpst_diff_log_id

#### Tags
    - object_name=chrg_rpst_diff_log
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}