{% docs sil__intermediate__dreams__price__cmpnt_prod_t_cleansed %}

#### Object Name
cmpnt_prod_t_cleansed

#### Object Definition
Additional information for component products, provides How the component/entitlement is distributed: Per Adult, Per Room, Per Person, Per Individual, Per Package, Per Child, Per Reservation, as well as when the component/entitlement is valid for, One Time, Per Meal Period, Per Meal Period Snack, Per Night, Per Once, And it also ties it to a default price sheet

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_prod_id & metadata_checksum combination.

#### Primary key
data_prod_id

#### Tags
    - object_name=cmpnt_prod_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__cmpnt_prod_t_versioned %}

#### Object Name
cmpnt_prod_t_versioned

#### Object Definition
Additional information for component products, provides How the component/entitlement is distributed: Per Adult, Per Room, Per Person, Per Individual, Per Package, Per Child, Per Reservation, as well as when the component/entitlement is valid for, One Time, Per Meal Period, Per Meal Period Snack, Per Night, Per Once, And it also ties it to a default price sheet

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_prod_id & metadata_checksum combination.

#### Primary key
data_prod_id

#### Tags
    - object_name=cmpnt_prod_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}