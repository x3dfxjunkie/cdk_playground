{% docs sil__intermediate__travelbox__west__gen_category_cleansed %}

#### Object Name
gen_category_cleansed

#### Object Definition
Contract level categorized product type(s) basic information defined under the selected element group in contract main panel. Set up at &#39;Categories&#39; branch of a contract tree in Contract Loading Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_category_no, data_contract_id & metadata_checksum combination.

#### Primary key
data_category_no, data_contract_id

#### Tags
    - object_name=gen_category
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__gen_category_versioned %}

#### Object Name
gen_category_versioned

#### Object Definition
Contract level categorized product type(s) basic information defined under the selected element group in contract main panel. Set up at &#39;Categories&#39; branch of a contract tree in Contract Loading Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_category_no, data_contract_id & metadata_checksum combination.

#### Primary key
data_category_no, data_contract_id

#### Tags
    - object_name=gen_category
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}