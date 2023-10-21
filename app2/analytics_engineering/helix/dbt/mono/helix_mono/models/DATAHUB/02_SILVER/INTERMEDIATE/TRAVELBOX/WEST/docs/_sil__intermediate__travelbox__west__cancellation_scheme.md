{% docs sil__intermediate__travelbox__west__cancellation_scheme_cleansed %}

#### Object Name
cancellation_scheme_cleansed

#### Object Definition
Contains user defined cancellation scheme details. Set up at Cancellation scheme main panel in Suplier Client

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cancel_scheme_id & metadata_checksum combination.

#### Primary key
data_cancel_scheme_id

#### Tags
    - object_name=cancellation_scheme
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__cancellation_scheme_versioned %}

#### Object Name
cancellation_scheme_versioned

#### Object Definition
Contains user defined cancellation scheme details. Set up at Cancellation scheme main panel in Suplier Client

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cancel_scheme_id & metadata_checksum combination.

#### Primary key
data_cancel_scheme_id

#### Tags
    - object_name=cancellation_scheme
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}