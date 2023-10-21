{% docs sil__intermediate__travelbox__east__acc_discount_cleansed %}

#### Object Name
acc_discount_cleansed

#### Object Definition
This table is used to store Discounts information. The values are setup in &#39;Discounts&#39; node in Accommodation Manager

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_contract_id, data_discount_no & metadata_checksum combination.

#### Primary key
data_contract_id, data_discount_no

#### Tags
    - object_name=acc_discount
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__acc_discount_versioned %}

#### Object Name
acc_discount_versioned

#### Object Definition
This table is used to store Discounts information. The values are setup in &#39;Discounts&#39; node in Accommodation Manager

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_contract_id, data_discount_no & metadata_checksum combination.

#### Primary key
data_contract_id, data_discount_no

#### Tags
    - object_name=acc_discount
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}