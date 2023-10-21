{% docs sil__intermediate__dreams__dining__acm_crus_cmpnt_cleansed %}

#### Object Name
acm_crus_cmpnt_cleansed

#### Object Definition
If the guest has booked a room reservation and a Disney Cruise Line reservation, the accommodation component provides the Ship code and the voyage number for the guests cruise.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acm_crus_cmpnt_id & metadata_checksum combination.

#### Primary key
data_acm_crus_cmpnt_id

#### Tags
    - object_name=acm_crus_cmpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__acm_crus_cmpnt_versioned %}

#### Object Name
acm_crus_cmpnt_versioned

#### Object Definition
If the guest has booked a room reservation and a Disney Cruise Line reservation, the accommodation component provides the Ship code and the voyage number for the guests cruise.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acm_crus_cmpnt_id & metadata_checksum combination.

#### Primary key
data_acm_crus_cmpnt_id

#### Tags
    - object_name=acm_crus_cmpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}