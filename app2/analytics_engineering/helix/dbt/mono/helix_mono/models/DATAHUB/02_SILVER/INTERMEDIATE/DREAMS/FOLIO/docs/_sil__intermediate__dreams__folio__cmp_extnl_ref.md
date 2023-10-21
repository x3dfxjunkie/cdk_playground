{% docs sil__intermediate__dreams__folio__cmp_extnl_ref_cleansed %}

#### Object Name
cmp_extnl_ref_cleansed

#### Object Definition
This table ties the charge market package ID to the Reservation Management Travel Component ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cmp_extnl_ref_id & metadata_checksum combination.

#### Primary key
data_cmp_extnl_ref_id

#### Tags
    - object_name=cmp_extnl_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__cmp_extnl_ref_versioned %}

#### Object Name
cmp_extnl_ref_versioned

#### Object Definition
This table ties the charge market package ID to the Reservation Management Travel Component ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cmp_extnl_ref_id & metadata_checksum combination.

#### Primary key
data_cmp_extnl_ref_id

#### Tags
    - object_name=cmp_extnl_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}