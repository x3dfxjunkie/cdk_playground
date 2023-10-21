{% docs sil__intermediate__dreams__entitlements__pos_cpn_prfl_t_cleansed %}

#### Table Name
pos_cpn_prfl_t_cleansed

#### Table Definition
This table associates the Point of Sale Coupon Profile ID to the Coupon Profile ID to provide the type of restrictions associated to the use of the coupon: CPN_RSTRCT_TYP_NM
        PER_PERSON_PER_NIGHT
        PER_PERSON_PER_TRAVEL_PLAN

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pos_cpn_prfl_id & metadata_checksum combination.

#### Primary key
data_pos_cpn_prfl_id

#### Tags
    - table_name=pos_cpn_prfl_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__pos_cpn_prfl_t_versioned %}

#### Table Name
pos_cpn_prfl_t_versioned

#### Table Definition
This table associates the Point of Sale Coupon Profile ID to the Coupon Profile ID to provide the type of restrictions associated to the use of the coupon: CPN_RSTRCT_TYP_NM
        PER_PERSON_PER_NIGHT
        PER_PERSON_PER_TRAVEL_PLAN

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pos_cpn_prfl_id & metadata_checksum combination.

#### Primary key
data_pos_cpn_prfl_id

#### Tags
    - table_name=pos_cpn_prfl_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}