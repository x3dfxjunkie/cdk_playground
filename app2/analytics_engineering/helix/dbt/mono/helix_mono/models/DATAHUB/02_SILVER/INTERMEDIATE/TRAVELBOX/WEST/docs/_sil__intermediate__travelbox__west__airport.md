{% docs sil__intermediate__travelbox__west__airport_cleansed %}

#### Object Name
airport_cleansed

#### Object Definition
Contains user defined airport location data to calculate the distance between departure and destination points. This will allow identifying the turnaround point of a travel itinerary which in turn will be used to calculate the fare. Set up at Setup Client.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=airport
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__airport_versioned %}

#### Object Name
airport_versioned

#### Object Definition
Contains user defined airport location data to calculate the distance between departure and destination points. This will allow identifying the turnaround point of a travel itinerary which in turn will be used to calculate the fare. Set up at Setup Client.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_code & metadata_checksum combination.

#### Primary key
data_code

#### Tags
    - object_name=airport
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}