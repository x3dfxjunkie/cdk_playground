{% docs sil__intermediate__travelbox__west__car_location_cleansed %}

#### Object Name
car_location_cleansed

#### Object Definition
Different locations available which can be used as pickup or drop off locations for a particular supplier, This can be setup from the Car module -&gt; setup -&gt; Location menu item -&gt; new Location dialog

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_location_id & metadata_checksum combination.

#### Primary key
data_location_id

#### Tags
    - object_name=car_location
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__west__car_location_versioned %}

#### Object Name
car_location_versioned

#### Object Definition
Different locations available which can be used as pickup or drop off locations for a particular supplier, This can be setup from the Car module -&gt; setup -&gt; Location menu item -&gt; new Location dialog

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_location_id & metadata_checksum combination.

#### Primary key
data_location_id

#### Tags
    - object_name=car_location
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}