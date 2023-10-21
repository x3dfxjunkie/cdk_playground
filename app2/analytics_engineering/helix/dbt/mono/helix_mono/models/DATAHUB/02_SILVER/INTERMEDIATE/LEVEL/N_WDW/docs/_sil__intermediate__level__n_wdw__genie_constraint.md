{% docs sil__intermediate__level__n_wdw__genie_constraint_cleansed %}

#### Object Name
genie_constraint_cleansed

#### Object Definition
Reference table for the &#39;constraints&#39; in Level N. A constraint is currently used for the Genie+ park specific products and contains what entitlements can be used in which park. For example, there are entitlements for Magic Kingdom only or for All 4 WDW parks.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_constraint_id & metadata_checksum combination.

#### Primary key
data_constraint_id

#### Tags
    - object_name=genie_constraint
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__genie_constraint_versioned %}

#### Object Name
genie_constraint_versioned

#### Object Definition
Reference table for the &#39;constraints&#39; in Level N. A constraint is currently used for the Genie+ park specific products and contains what entitlements can be used in which park. For example, there are entitlements for Magic Kingdom only or for All 4 WDW parks.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_constraint_id & metadata_checksum combination.

#### Primary key
data_constraint_id

#### Tags
    - object_name=genie_constraint
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}