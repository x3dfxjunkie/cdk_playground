{% docs sil__intermediate__dreams__rooms_reservations__tc_grp_typ_cleansed %}

#### Object Name
tc_grp_typ_cleansed

#### Object Definition
Provides the types of travel component grouping  ie: TC_GRP_TYP_NM ACCOMMODATION, ACTIVITY, ADD_ON_PACKAGE, ADMISSION, CIRQUE, COMP_TICKET, DAY_GUEST_TICKET, DME, EVENTDINING, FOODANDBEVERAGE, HARD_TICKET_EVENT, ONETIMEUSEPOINTS, PACKAGE, SHOWDINING, SPA, TABLESERVICEDINING

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_grp_typ_nm & metadata_checksum combination.

#### Primary key
data_tc_grp_typ_nm

#### Tags
    - object_name=tc_grp_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tc_grp_typ_versioned %}

#### Object Name
tc_grp_typ_versioned

#### Object Definition
Provides the types of travel component grouping  ie: TC_GRP_TYP_NM ACCOMMODATION, ACTIVITY, ADD_ON_PACKAGE, ADMISSION, CIRQUE, COMP_TICKET, DAY_GUEST_TICKET, DME, EVENTDINING, FOODANDBEVERAGE, HARD_TICKET_EVENT, ONETIMEUSEPOINTS, PACKAGE, SHOWDINING, SPA, TABLESERVICEDINING

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_grp_typ_nm & metadata_checksum combination.

#### Primary key
data_tc_grp_typ_nm

#### Tags
    - object_name=tc_grp_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}