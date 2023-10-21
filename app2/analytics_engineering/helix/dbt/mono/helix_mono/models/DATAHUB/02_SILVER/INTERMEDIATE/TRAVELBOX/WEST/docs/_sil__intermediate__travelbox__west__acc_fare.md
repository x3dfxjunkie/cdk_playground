{% docs sil__intermediate__travelbox__west__acc_fare_cleansed %}

#### Object Name
acc_fare_cleansed

#### Object Definition
This table is used to store Room/Apartment fare information when Rate Type is &#39;Per Person&#39;. The values are setup in &#39;Rooms&#39; node in Accommodation Manager

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_contract_id, data_fare_no, data_room_apt_no & metadata_checksum combination.

#### Primary key
data_contract_id, data_fare_no, data_room_apt_no

#### Tags
    - object_name=acc_fare
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__acc_fare_versioned %}

#### Object Name
acc_fare_versioned

#### Object Definition
This table is used to store Room/Apartment fare information when Rate Type is &#39;Per Person&#39;. The values are setup in &#39;Rooms&#39; node in Accommodation Manager

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_contract_id, data_fare_no, data_room_apt_no & metadata_checksum combination.

#### Primary key
data_contract_id, data_fare_no, data_room_apt_no

#### Tags
    - object_name=acc_fare
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}