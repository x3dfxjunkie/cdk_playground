{% docs sil__intermediate__travelbox__west__pax_sub_type_cleansed %}

#### Object Name
pax_sub_type_cleansed

#### Object Definition
Different types of passengers based off the default passenger types. Set up under &#39;Pax Types&#39; in &#39;General&#39; menu of Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=pax_sub_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__pax_sub_type_versioned %}

#### Object Name
pax_sub_type_versioned

#### Object Definition
Different types of passengers based off the default passenger types. Set up under &#39;Pax Types&#39; in &#39;General&#39; menu of Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=pax_sub_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}