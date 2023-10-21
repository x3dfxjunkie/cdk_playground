{% docs sil__intermediate__dreams__folio__chrg_mkt_pkg_cleansed %}

#### Object Name
chrg_mkt_pkg_cleansed

#### Object Definition
Ties the PKG ID and Description to a Charge Market Package ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrg_mkt_pkg_id & metadata_checksum combination.

#### Primary key
data_chrg_mkt_pkg_id

#### Tags
    - object_name=chrg_mkt_pkg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__chrg_mkt_pkg_versioned %}

#### Object Name
chrg_mkt_pkg_versioned

#### Object Definition
Ties the PKG ID and Description to a Charge Market Package ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrg_mkt_pkg_id & metadata_checksum combination.

#### Primary key
data_chrg_mkt_pkg_id

#### Tags
    - object_name=chrg_mkt_pkg
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}