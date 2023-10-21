{% docs sil__intermediate__dreams__rooms_fulfillment__sls_chan_cleansed %}

#### Object Name
sls_chan_cleansed

#### Object Definition
The individual or organization that has brought the reservation to WDW or Aulani

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_sls_chan_id & metadata_checksum combination.

#### Primary key
data_sls_chan_id

#### Tags
    - object_name=sls_chan
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__sls_chan_versioned %}

#### Object Name
sls_chan_versioned

#### Object Definition
The individual or organization that has brought the reservation to WDW or Aulani

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_sls_chan_id & metadata_checksum combination.

#### Primary key
data_sls_chan_id

#### Tags
    - object_name=sls_chan
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}