{% docs sil__intermediate__travelbox__west__acc_room_apartment_type_cleansed %}

#### Object Name
acc_room_apartment_type_cleansed

#### Object Definition
This table is used to store Room/Apartment Types information. The values are setup in Accommodation Manager-&gt;Setup-&gt;Room/Apartment Types

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=acc_room_apartment_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__acc_room_apartment_type_versioned %}

#### Object Name
acc_room_apartment_type_versioned

#### Object Definition
This table is used to store Room/Apartment Types information. The values are setup in Accommodation Manager-&gt;Setup-&gt;Room/Apartment Types

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=acc_room_apartment_type
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}