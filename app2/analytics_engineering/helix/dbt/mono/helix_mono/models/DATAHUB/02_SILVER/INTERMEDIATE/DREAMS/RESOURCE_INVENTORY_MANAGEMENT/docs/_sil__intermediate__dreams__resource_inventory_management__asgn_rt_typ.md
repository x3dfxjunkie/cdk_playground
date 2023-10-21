{% docs sil__intermediate__dreams__resource_inventory_management__asgn_rt_typ_cleansed %}

#### Object Name
asgn_rt_typ_cleansed

#### Object Definition
This table contains the rate category codes without any known FKs:
                        GEN
                        GRP
                        PAR
                        SP1
                        SP2
                        SP3
                        SP4
                        UPS
                    

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_rsrt_asgn_scr_id, data_rt_typ_nm & metadata_checksum combination.

#### Primary key
data_rsrt_asgn_scr_id, data_rt_typ_nm

#### Tags
    - object_name=asgn_rt_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__asgn_rt_typ_versioned %}

#### Object Name
asgn_rt_typ_versioned

#### Object Definition
This table contains the rate category codes without any known FKs:
                        GEN
                        GRP
                        PAR
                        SP1
                        SP2
                        SP3
                        SP4
                        UPS
                    

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_rsrt_asgn_scr_id, data_rt_typ_nm & metadata_checksum combination.

#### Primary key
data_rsrt_asgn_scr_id, data_rt_typ_nm

#### Tags
    - object_name=asgn_rt_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}