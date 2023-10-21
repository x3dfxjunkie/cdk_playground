{% docs sil__intermediate__dreams__rooms_reservations__tc_gst_cleansed %}

#### Object Name
tc_gst_cleansed

#### Object Definition
This table provides the age type and age number for the guests associated to that travel component, as well as the transactional individual ID and the visit purpose.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_gst_id & metadata_checksum combination.

#### Primary key
data_tc_gst_id

#### Tags
    - object_name=tc_gst
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tc_gst_versioned %}

#### Object Name
tc_gst_versioned

#### Object Definition
This table provides the age type and age number for the guests associated to that travel component, as well as the transactional individual ID and the visit purpose.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_gst_id & metadata_checksum combination.

#### Primary key
data_tc_gst_id

#### Tags
    - object_name=tc_gst
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}