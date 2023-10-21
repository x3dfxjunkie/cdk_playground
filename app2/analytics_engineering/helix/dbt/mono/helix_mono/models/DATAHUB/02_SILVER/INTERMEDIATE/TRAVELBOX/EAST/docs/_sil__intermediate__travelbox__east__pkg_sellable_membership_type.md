{% docs sil__intermediate__travelbox__east__pkg_sellable_membership_type_cleansed %}

#### Object Name
pkg_sellable_membership_type_cleansed

#### Object Definition
Setup at the Sales Parameters node of the package tree. Membership types for which this package can be
sold are stored

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_membership_type, data_pkg_group_id & metadata_checksum combination.

#### Primary key
data_membership_type, data_pkg_group_id

#### Tags
    - object_name=pkg_sellable_membership_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__pkg_sellable_membership_type_versioned %}

#### Object Name
pkg_sellable_membership_type_versioned

#### Object Definition
Setup at the Sales Parameters node of the package tree. Membership types for which this package can be
sold are stored

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_membership_type, data_pkg_group_id & metadata_checksum combination.

#### Primary key
data_membership_type, data_pkg_group_id

#### Tags
    - object_name=pkg_sellable_membership_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}