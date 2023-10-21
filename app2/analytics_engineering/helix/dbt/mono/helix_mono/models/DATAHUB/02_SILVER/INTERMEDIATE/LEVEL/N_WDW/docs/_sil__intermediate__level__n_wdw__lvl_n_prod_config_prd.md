{% docs sil__intermediate__level__n_wdw__lvl_n_prod_config_prd_cleansed %}

#### Object Name
lvl_n_prod_config_prd_cleansed

#### Object Definition
Reference table for the product configuration period name and the description.  Source table has only one row and not further populated since 2012.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_lvl_n_prod_config_prd_nm & metadata_checksum combination.

#### Primary key
data_lvl_n_prod_config_prd_nm

#### Tags
    - object_name=lvl_n_prod_config_prd
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__lvl_n_prod_config_prd_versioned %}

#### Object Name
lvl_n_prod_config_prd_versioned

#### Object Definition
Reference table for the product configuration period name and the description.  Source table has only one row and not further populated since 2012.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_lvl_n_prod_config_prd_nm & metadata_checksum combination.

#### Primary key
data_lvl_n_prod_config_prd_nm

#### Tags
    - object_name=lvl_n_prod_config_prd
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}