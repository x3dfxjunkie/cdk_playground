{% docs sil__intermediate__dreams__price__feat_t_cleansed %}

#### Object Name
feat_t_cleansed

#### Object Definition
List of features: Sales Tax - Beaufort County (SC) - Merchandise, Communications Tax - Beaufort County (SC), Adjust for Discount, Sales Tax - Beaufort County (SC) - Food, Osceola County Accommodation Tax, Osceola County Tourist Development Tax, Indian River

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_feat_id & metadata_checksum combination.

#### Primary key
data_feat_id

#### Tags
    - object_name=feat_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__feat_t_versioned %}

#### Object Name
feat_t_versioned

#### Object Definition
List of features: Sales Tax - Beaufort County (SC) - Merchandise, Communications Tax - Beaufort County (SC), Adjust for Discount, Sales Tax - Beaufort County (SC) - Food, Osceola County Accommodation Tax, Osceola County Tourist Development Tax, Indian River

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_feat_id & metadata_checksum combination.

#### Primary key
data_feat_id

#### Tags
    - object_name=feat_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}