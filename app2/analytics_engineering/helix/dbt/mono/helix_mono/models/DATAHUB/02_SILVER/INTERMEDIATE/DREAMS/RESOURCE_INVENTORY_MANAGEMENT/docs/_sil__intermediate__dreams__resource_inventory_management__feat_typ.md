{% docs sil__intermediate__dreams__resource_inventory_management__feat_typ_cleansed %}

#### Object Name
feat_typ_cleansed

#### Object Definition
Holds the feature type names and their descriptions: FEAT_TYP_NM
Additional Bedding
Proximity
Pets
Wing
Floor Type
Cluster
Wing test
Theme
Building
View
Bedding
VIP
Area
TV Theme
Side
Connect
Physical
wing test A
Special
Floor

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_feat_typ_nm & metadata_checksum combination.

#### Primary key
data_feat_typ_nm

#### Tags
    - object_name=feat_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__feat_typ_versioned %}

#### Object Name
feat_typ_versioned

#### Object Definition
Holds the feature type names and their descriptions: FEAT_TYP_NM
Additional Bedding
Proximity
Pets
Wing
Floor Type
Cluster
Wing test
Theme
Building
View
Bedding
VIP
Area
TV Theme
Side
Connect
Physical
wing test A
Special
Floor

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_feat_typ_nm & metadata_checksum combination.

#### Primary key
data_feat_typ_nm

#### Tags
    - object_name=feat_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}