{% docs sil__intermediate__dreams__price__pkg_prod_cls_t_cleansed %}

#### Object Name
pkg_prod_cls_t_cleansed

#### Object Definition
This table provides the product classification ID associated to the product and some additional information about the package

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pkg_prod_cls_id & metadata_checksum combination.

#### Primary key
data_pkg_prod_cls_id

#### Tags
    - object_name=pkg_prod_cls_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__pkg_prod_cls_t_versioned %}

#### Object Name
pkg_prod_cls_t_versioned

#### Object Definition
This table provides the product classification ID associated to the product and some additional information about the package

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pkg_prod_cls_id & metadata_checksum combination.

#### Primary key
data_pkg_prod_cls_id

#### Tags
    - object_name=pkg_prod_cls_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}