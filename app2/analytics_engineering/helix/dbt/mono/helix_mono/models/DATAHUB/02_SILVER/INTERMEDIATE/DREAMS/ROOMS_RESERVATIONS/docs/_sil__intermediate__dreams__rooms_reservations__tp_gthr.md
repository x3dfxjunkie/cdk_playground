{% docs sil__intermediate__dreams__rooms_reservations__tp_gthr_cleansed %}

#### Object Name
tp_gthr_cleansed

#### Object Definition
This table provides an association between travel parties who have separate reservations. It&#39;s called Gather Code that is a retired product we had, it&#39;s better known as a Travel With Code.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_gthr_cd, data_tp_id & metadata_checksum combination.

#### Primary key
data_gthr_cd, data_tp_id

#### Tags
    - object_name=tp_gthr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tp_gthr_versioned %}

#### Object Name
tp_gthr_versioned

#### Object Definition
This table provides an association between travel parties who have separate reservations. It&#39;s called Gather Code that is a retired product we had, it&#39;s better known as a Travel With Code.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_gthr_cd, data_tp_id & metadata_checksum combination.

#### Primary key
data_gthr_cd, data_tp_id

#### Tags
    - object_name=tp_gthr
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}