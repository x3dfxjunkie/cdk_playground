{% docs sil__intermediate__dreams__rooms_reservations__tc_typ_cleansed %}

#### Object Name
tc_typ_cleansed

#### Object Definition
List of travel component types:AccommodationComponent, Service, PackageTravelComponent, AdmissionComponent, ComponentTravelComponent

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_tc_typ_nm & metadata_checksum combination.

#### Primary key
data_tc_typ_nm

#### Tags
    - object_name=tc_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__tc_typ_versioned %}

#### Object Name
tc_typ_versioned

#### Object Definition
List of travel component types:AccommodationComponent, Service, PackageTravelComponent, AdmissionComponent, ComponentTravelComponent

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_tc_typ_nm & metadata_checksum combination.

#### Primary key
data_tc_typ_nm

#### Tags
    - object_name=tc_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}