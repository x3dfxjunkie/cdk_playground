{% docs sil__intermediate__travelbox__west__payment_scheme_cleansed %}

#### Object Name
payment_scheme_cleansed

#### Object Definition
Globally defined payment scheme informations are stored here. Set up under &#39;Payment Schemes&#39; in &#39;Setup&#39; menu of Supplier Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pay_scheme_id & metadata_checksum combination.

#### Primary key
data_pay_scheme_id

#### Tags
    - object_name=payment_scheme
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__payment_scheme_versioned %}

#### Object Name
payment_scheme_versioned

#### Object Definition
Globally defined payment scheme informations are stored here. Set up under &#39;Payment Schemes&#39; in &#39;Setup&#39; menu of Supplier Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pay_scheme_id & metadata_checksum combination.

#### Primary key
data_pay_scheme_id

#### Tags
    - object_name=payment_scheme
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}