{% docs sil__intermediate__travelbox__east__cmp_company_cleansed %}

#### Object Name
cmp_company_cleansed

#### Object Definition
This is the table for travelbox company details. Set up under &#39;Company&#39; in &#39;General&#39; tab of Set up Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=cmp_company
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__cmp_company_versioned %}

#### Object Name
cmp_company_versioned

#### Object Definition
This is the table for travelbox company details. Set up under &#39;Company&#39; in &#39;General&#39; tab of Set up Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=cmp_company
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}