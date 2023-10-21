{% docs sil__intermediate__travelbox__west__gen_discount_cleansed %}

#### Object Name
gen_discount_cleansed

#### Object Definition
Discount information of a particular discount defined at &#39;Discounts&#39; branch of a generic contract in Generiic Loading Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_contract_id, data_discount_no & metadata_checksum combination.

#### Primary key
data_contract_id, data_discount_no

#### Tags
    - object_name=gen_discount
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__gen_discount_versioned %}

#### Object Name
gen_discount_versioned

#### Object Definition
Discount information of a particular discount defined at &#39;Discounts&#39; branch of a generic contract in Generiic Loading Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_contract_id, data_discount_no & metadata_checksum combination.

#### Primary key
data_contract_id, data_discount_no

#### Tags
    - object_name=gen_discount
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}