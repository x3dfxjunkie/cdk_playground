{% docs sil__intermediate__xbms__wdw__cost_ctr_cleansed %}

#### Object Name
cost_ctr_cleansed

#### Object Definition
Reference table for cost center IDs, their codes and descriptions.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cost_ctr_id & metadata_checksum combination.

#### Primary key
data_cost_ctr_id

#### Tags
    - object_name=cost_ctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__cost_ctr_versioned %}

#### Object Name
cost_ctr_versioned

#### Object Definition
Reference table for cost center IDs, their codes and descriptions.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cost_ctr_id & metadata_checksum combination.

#### Primary key
data_cost_ctr_id

#### Tags
    - object_name=cost_ctr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}