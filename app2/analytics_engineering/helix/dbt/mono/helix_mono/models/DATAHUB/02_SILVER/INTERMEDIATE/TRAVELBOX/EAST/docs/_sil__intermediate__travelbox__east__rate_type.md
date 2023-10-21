{% docs sil__intermediate__travelbox__east__rate_type_cleansed %}

#### Object Name
rate_type_cleansed

#### Object Definition
This table contains the text lables defined for each pre-defined rate types and the display restrictions of thier properties. Set up at &#39;Rate Types&#39; under &#39;Contracting&#39; menu in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=rate_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__rate_type_versioned %}

#### Object Name
rate_type_versioned

#### Object Definition
This table contains the text lables defined for each pre-defined rate types and the display restrictions of thier properties. Set up at &#39;Rate Types&#39; under &#39;Contracting&#39; menu in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=rate_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}