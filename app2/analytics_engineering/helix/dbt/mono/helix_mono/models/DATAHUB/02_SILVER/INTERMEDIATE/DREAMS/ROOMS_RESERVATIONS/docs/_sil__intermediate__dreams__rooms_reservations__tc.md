{% docs sil__intermediate__dreams__rooms_reservations__tc_cleansed %}

#### Object Name
tc_cleansed

#### Object Definition
This table holds information about the detailed parts, items, components of the reservation and/or the package ie: AccommodationComponent; Service; PackageTravelComponent; AdmissionComponent; ComponentTravelComponent)

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_id & metadata_checksum combination.

#### Primary key
data_tc_id

#### Tags
    - object_name=tc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tc_versioned %}

#### Object Name
tc_versioned

#### Object Definition
This table holds information about the detailed parts, items, components of the reservation and/or the package ie: AccommodationComponent; Service; PackageTravelComponent; AdmissionComponent; ComponentTravelComponent)

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_id & metadata_checksum combination.

#### Primary key
data_tc_id

#### Tags
    - object_name=tc
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}