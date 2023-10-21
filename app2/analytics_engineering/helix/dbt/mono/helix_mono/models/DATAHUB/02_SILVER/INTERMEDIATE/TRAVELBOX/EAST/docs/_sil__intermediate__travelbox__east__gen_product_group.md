{% docs sil__intermediate__travelbox__east__gen_product_group_cleansed %}

#### Object Name
gen_product_group_cleansed

#### Object Definition
This contains the element groups list used for generic contracts. Set up at &#39;Element Groups&#39; menu item in Setup menu of Generic Loading Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_product_id & metadata_checksum combination.

#### Primary key
data_product_id

#### Tags
    - object_name=gen_product_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__gen_product_group_versioned %}

#### Object Name
gen_product_group_versioned

#### Object Definition
This contains the element groups list used for generic contracts. Set up at &#39;Element Groups&#39; menu item in Setup menu of Generic Loading Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_product_id & metadata_checksum combination.

#### Primary key
data_product_id

#### Tags
    - object_name=gen_product_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}