{% docs sil__intermediate__dreams__folio__ta_comm_rt_spec_cleansed %}

#### Object Name
ta_comm_rt_spec_cleansed

#### Object Definition
This table provides the commission  rate information on select reservation components for Travel Agencies

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_comm_rt_spec_id & metadata_checksum combination.

#### Primary key
data_comm_rt_spec_id

#### Tags
    - object_name=ta_comm_rt_spec
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__ta_comm_rt_spec_versioned %}

#### Object Name
ta_comm_rt_spec_versioned

#### Object Definition
This table provides the commission  rate information on select reservation components for Travel Agencies

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_comm_rt_spec_id & metadata_checksum combination.

#### Primary key
data_comm_rt_spec_id

#### Tags
    - object_name=ta_comm_rt_spec
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}