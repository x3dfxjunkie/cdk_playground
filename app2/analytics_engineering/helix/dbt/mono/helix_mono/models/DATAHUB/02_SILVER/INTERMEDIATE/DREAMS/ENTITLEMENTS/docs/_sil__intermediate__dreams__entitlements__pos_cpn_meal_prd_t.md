{% docs sil__intermediate__dreams__entitlements__pos_cpn_meal_prd_t_cleansed %}

#### Table Name
pos_cpn_meal_prd_t_cleansed

#### Table Definition
This table associates the Point of Sale Profile ID to the Point of Sale Meal Period codes: CPN_MEAL_PRD_NM
        0
        00
        01
        04
        05

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pos_cpn_meal_prd_id & metadata_checksum combination.

#### Primary key
data_pos_cpn_meal_prd_id

#### Tags
    - table_name=pos_cpn_meal_prd_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__pos_cpn_meal_prd_t_versioned %}

#### Table Name
pos_cpn_meal_prd_t_versioned

#### Table Definition
This table associates the Point of Sale Profile ID to the Point of Sale Meal Period codes: CPN_MEAL_PRD_NM
        0
        00
        01
        04
        05

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pos_cpn_meal_prd_id & metadata_checksum combination.

#### Primary key
data_pos_cpn_meal_prd_id

#### Tags
    - table_name=pos_cpn_meal_prd_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}