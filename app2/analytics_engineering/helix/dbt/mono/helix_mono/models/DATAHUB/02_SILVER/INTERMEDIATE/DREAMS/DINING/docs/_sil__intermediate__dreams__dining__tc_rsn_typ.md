{% docs sil__intermediate__dreams__dining__tc_rsn_typ_cleansed %}

#### Object Name
tc_rsn_typ_cleansed

#### Object Definition
The distinct list of Reason types: TC_RSN_TYP_NM A la Carte Cancel Cancel Change Complimentary Ticket Early Checkout Fee Waive Inventory Override Mass Cancel Rate Override Reinstate Ticket Reprint Upgrade

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_rsn_typ_nm & metadata_checksum combination.

#### Primary key
data_tc_rsn_typ_nm

#### Tags
    - object_name=tc_rsn_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__tc_rsn_typ_versioned %}

#### Object Name
tc_rsn_typ_versioned

#### Object Definition
The distinct list of Reason types: TC_RSN_TYP_NM A la Carte Cancel Cancel Change Complimentary Ticket Early Checkout Fee Waive Inventory Override Mass Cancel Rate Override Reinstate Ticket Reprint Upgrade

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_rsn_typ_nm & metadata_checksum combination.

#### Primary key
data_tc_rsn_typ_nm

#### Tags
    - object_name=tc_rsn_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}