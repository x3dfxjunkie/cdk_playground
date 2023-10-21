{% docs sil__intermediate__travelbox__east__trs_mode_cleansed %}

#### Object Name
trs_mode_cleansed

#### Object Definition
Table contains the transfer modes. This can be setup in the transfer manager-&gt; setup menu -&gt;  transfer modes. Ex. Car

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=trs_mode
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__trs_mode_versioned %}

#### Object Name
trs_mode_versioned

#### Object Definition
Table contains the transfer modes. This can be setup in the transfer manager-&gt; setup menu -&gt;  transfer modes. Ex. Car

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=trs_mode
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}