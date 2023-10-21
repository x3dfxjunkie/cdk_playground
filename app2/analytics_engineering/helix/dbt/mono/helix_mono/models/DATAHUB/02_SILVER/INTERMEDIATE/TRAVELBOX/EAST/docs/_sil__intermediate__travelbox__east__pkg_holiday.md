{% docs sil__intermediate__travelbox__east__pkg_holiday_cleansed %}

#### Object Name
pkg_holiday_cleansed

#### Object Definition
Represents a particular version of a package. Primary details such as  of a package
package_id, group_id, version number and valid periods are stored.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_package_id & metadata_checksum combination.

#### Primary key
data_package_id

#### Tags
    - object_name=pkg_holiday
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__pkg_holiday_versioned %}

#### Object Name
pkg_holiday_versioned

#### Object Definition
Represents a particular version of a package. Primary details such as  of a package
package_id, group_id, version number and valid periods are stored.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_package_id & metadata_checksum combination.

#### Primary key
data_package_id

#### Tags
    - object_name=pkg_holiday
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}