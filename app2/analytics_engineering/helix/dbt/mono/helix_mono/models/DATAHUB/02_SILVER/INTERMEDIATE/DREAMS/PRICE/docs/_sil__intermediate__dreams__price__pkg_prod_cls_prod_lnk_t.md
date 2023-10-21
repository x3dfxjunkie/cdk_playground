{% docs sil__intermediate__dreams__price__pkg_prod_cls_prod_lnk_t_cleansed %}

#### Object Name
pkg_prod_cls_prod_lnk_t_cleansed

#### Object Definition
This table provides the IDs to associate the package to product classification and the product link table

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pkg_prod_cls_id, data_prod_lnk_id & metadata_checksum combination.

#### Primary key
data_pkg_prod_cls_id, data_prod_lnk_id

#### Tags
    - object_name=pkg_prod_cls_prod_lnk_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__pkg_prod_cls_prod_lnk_t_versioned %}

#### Object Name
pkg_prod_cls_prod_lnk_t_versioned

#### Object Definition
This table provides the IDs to associate the package to product classification and the product link table

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pkg_prod_cls_id, data_prod_lnk_id & metadata_checksum combination.

#### Primary key
data_pkg_prod_cls_id, data_prod_lnk_id

#### Tags
    - object_name=pkg_prod_cls_prod_lnk_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}