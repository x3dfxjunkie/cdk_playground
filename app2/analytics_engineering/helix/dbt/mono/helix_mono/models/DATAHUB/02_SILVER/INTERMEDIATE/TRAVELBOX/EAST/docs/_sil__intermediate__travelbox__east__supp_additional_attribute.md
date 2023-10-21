{% docs sil__intermediate__travelbox__east__supp_additional_attribute_cleansed %}

#### Object Name
supp_additional_attribute_cleansed

#### Object Definition
This contains the values for generic supplier attributes. Setup at &#39;Attributes&#39; branch of a &#39;Supplier&#39; tree in Supplier Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code, data_supplier_id & metadata_checksum combination.

#### Primary key
data_code, data_supplier_id

#### Tags
    - object_name=supp_additional_attribute
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__supp_additional_attribute_versioned %}

#### Object Name
supp_additional_attribute_versioned

#### Object Definition
This contains the values for generic supplier attributes. Setup at &#39;Attributes&#39; branch of a &#39;Supplier&#39; tree in Supplier Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code, data_supplier_id & metadata_checksum combination.

#### Primary key
data_code, data_supplier_id

#### Tags
    - object_name=supp_additional_attribute
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}