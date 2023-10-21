{% docs sil__intermediate__travelbox__east__pkg_itinerary_cleansed %}

#### Object Name
pkg_itinerary_cleansed

#### Object Definition
Details such as package_id, Itinerary_no, name and code of the itinerary are stored.
Itineraries are setup at the itineraries node of the package tree

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_itinerary_no, data_package_id & metadata_checksum combination.

#### Primary key
data_itinerary_no, data_package_id

#### Tags
    - object_name=pkg_itinerary
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__pkg_itinerary_versioned %}

#### Object Name
pkg_itinerary_versioned

#### Object Definition
Details such as package_id, Itinerary_no, name and code of the itinerary are stored.
Itineraries are setup at the itineraries node of the package tree

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_itinerary_no, data_package_id & metadata_checksum combination.

#### Primary key
data_itinerary_no, data_package_id

#### Tags
    - object_name=pkg_itinerary
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}