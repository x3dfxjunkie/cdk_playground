{% docs sil__intermediate__dreams__price__fac_prod_t_cleansed %}

#### Object Name
fac_prod_t_cleansed

#### Object Definition
Associates products to enterprise facility IDs

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_fac_id, data_fac_prod_typ_nm, data_prod_id & metadata_checksum combination.

#### Primary key
data_fac_id, data_fac_prod_typ_nm, data_prod_id

#### Tags
    - object_name=fac_prod_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__fac_prod_t_versioned %}

#### Object Name
fac_prod_t_versioned

#### Object Definition
Associates products to enterprise facility IDs

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_fac_id, data_fac_prod_typ_nm, data_prod_id & metadata_checksum combination.

#### Primary key
data_fac_id, data_fac_prod_typ_nm, data_prod_id

#### Tags
    - object_name=fac_prod_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}