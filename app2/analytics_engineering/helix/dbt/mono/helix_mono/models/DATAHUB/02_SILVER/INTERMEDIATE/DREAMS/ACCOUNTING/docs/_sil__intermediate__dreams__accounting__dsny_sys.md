{% docs sil__intermediate__dreams__accounting__dsny_sys_cleansed %}

#### Object Name
dsny_sys_cleansed

#### Object Definition
A list of Codes related to Disney and the Disney system names the correlate with. Examples: Walt Disney World Scheduled Events Back Office
Pacific Region Lilo Express Checkout
Walt Disney World Scheduled Events Call Center
Walt Disney World DREAMS Back Office
Walt Disney World DREAMS Internet

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_dsny_sys_cd & metadata_checksum combination.

#### Primary key
data_dsny_sys_cd

#### Tags
    - object_name=dsny_sys
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__dsny_sys_versioned %}

#### Object Name
dsny_sys_versioned

#### Object Definition
A list of Codes related to Disney and the Disney system names the correlate with. Examples: Walt Disney World Scheduled Events Back Office
Pacific Region Lilo Express Checkout
Walt Disney World Scheduled Events Call Center
Walt Disney World DREAMS Back Office
Walt Disney World DREAMS Internet

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_dsny_sys_cd & metadata_checksum combination.

#### Primary key
data_dsny_sys_cd

#### Tags
    - object_name=dsny_sys
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}