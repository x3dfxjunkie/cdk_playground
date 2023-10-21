{% docs sil__intermediate__dreams__price__adm_prod_t_cleansed %}

#### Object Name
adm_prod_t_cleansed

#### Object Definition
Provides additional product information for Admission products ie: The number of days the guest tickets is valid for 1,4,3,5,6,2,365,7,9,10,421,450,12,11,0,8,13

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_adm_prod_id & metadata_checksum combination.

#### Primary key
data_adm_prod_id

#### Tags
    - object_name=adm_prod_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__adm_prod_t_versioned %}

#### Object Name
adm_prod_t_versioned

#### Object Definition
Provides additional product information for Admission products ie: The number of days the guest tickets is valid for 1,4,3,5,6,2,365,7,9,10,421,450,12,11,0,8,13

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_adm_prod_id & metadata_checksum combination.

#### Primary key
data_adm_prod_id

#### Tags
    - object_name=adm_prod_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}