{% docs sil__intermediate__travelbox__west__gen_supplement_category_cleansed %}

#### Object Name
gen_supplement_category_cleansed

#### Object Definition
Generic Supplement categories list which is used to categorize the supplement of a Generic contract. Setup under &#39;Supplement Categories&#39; of &#39;Setup&#39; menu in Generic Loading Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_category_id & metadata_checksum combination.

#### Primary key
data_category_id

#### Tags
    - object_name=gen_supplement_category
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__gen_supplement_category_versioned %}

#### Object Name
gen_supplement_category_versioned

#### Object Definition
Generic Supplement categories list which is used to categorize the supplement of a Generic contract. Setup under &#39;Supplement Categories&#39; of &#39;Setup&#39; menu in Generic Loading Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_category_id & metadata_checksum combination.

#### Primary key
data_category_id

#### Tags
    - object_name=gen_supplement_category
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}