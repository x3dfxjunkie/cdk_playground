{% docs sil__intermediate__dreams__profile__prfl_rte_typ_cleansed %}

#### Object Name
prfl_rte_typ_cleansed

#### Object Definition
List of different profile route types: PRFL_RTE_TYP_NM; AutoFulfillment; Celebrations; Dispatch System; Guest History; Guest Recovery; Guest Request; HouseKeeping; Inventory; Reservation; Reservation and Confirmation; Resort Call Center; SE SPL Needs; SPL Event

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_prfl_rte_typ_nm & metadata_checksum combination.

#### Primary key
data_prfl_rte_typ_nm

#### Tags
    - object_name=prfl_rte_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__profile__prfl_rte_typ_versioned %}

#### Object Name
prfl_rte_typ_versioned

#### Object Definition
List of different profile route types: PRFL_RTE_TYP_NM; AutoFulfillment; Celebrations; Dispatch System; Guest History; Guest Recovery; Guest Request; HouseKeeping; Inventory; Reservation; Reservation and Confirmation; Resort Call Center; SE SPL Needs; SPL Event

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_prfl_rte_typ_nm & metadata_checksum combination.

#### Primary key
data_prfl_rte_typ_nm

#### Tags
    - object_name=prfl_rte_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}