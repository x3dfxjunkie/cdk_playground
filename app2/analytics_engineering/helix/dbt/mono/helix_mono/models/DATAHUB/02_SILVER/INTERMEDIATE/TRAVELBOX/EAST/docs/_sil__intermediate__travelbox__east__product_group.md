{% docs sil__intermediate__travelbox__east__product_group_cleansed %}

#### Object Name
product_group_cleansed

#### Object Definition
Product groups which are used for classifying package holidays in TravelBox. Set up under &#39;Coding Levels&#39; menu in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=product_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__product_group_versioned %}

#### Object Name
product_group_versioned

#### Object Definition
Product groups which are used for classifying package holidays in TravelBox. Set up under &#39;Coding Levels&#39; menu in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=product_group
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}