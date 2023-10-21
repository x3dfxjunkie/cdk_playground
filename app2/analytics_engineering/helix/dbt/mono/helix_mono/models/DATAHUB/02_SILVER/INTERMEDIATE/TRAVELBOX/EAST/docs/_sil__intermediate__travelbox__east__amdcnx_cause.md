{% docs sil__intermediate__travelbox__east__amdcnx_cause_cleansed %}

#### Object Name
amdcnx_cause_cleansed

#### Object Definition
This contains predefining causes for an amendment or cancellation of a booking. Set up at Reservation in Setup Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=amdcnx_cause
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__amdcnx_cause_versioned %}

#### Object Name
amdcnx_cause_versioned

#### Object Definition
This contains predefining causes for an amendment or cancellation of a booking. Set up at Reservation in Setup Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_id & metadata_checksum combination.

#### Primary key
data_id

#### Tags
    - object_name=amdcnx_cause
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}