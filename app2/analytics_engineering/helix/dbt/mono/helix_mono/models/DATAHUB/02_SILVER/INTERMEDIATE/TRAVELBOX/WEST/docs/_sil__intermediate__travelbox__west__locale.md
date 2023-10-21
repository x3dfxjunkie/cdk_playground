{% docs sil__intermediate__travelbox__west__locale_cleansed %}

#### Object Name
locale_cleansed

#### Object Definition
This table contains the Travelbox locales which are used in Content Manager. Set up at &#39;Locale&#39; under Setup menu in Customer Profiles Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=locale
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__locale_versioned %}

#### Object Name
locale_versioned

#### Object Definition
This table contains the Travelbox locales which are used in Content Manager. Set up at &#39;Locale&#39; under Setup menu in Customer Profiles Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=locale
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}