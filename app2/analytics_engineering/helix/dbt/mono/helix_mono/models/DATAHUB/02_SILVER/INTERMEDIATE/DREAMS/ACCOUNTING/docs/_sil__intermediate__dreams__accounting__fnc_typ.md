{% docs sil__intermediate__dreams__accounting__fnc_typ_cleansed %}

#### Object Name
fnc_typ_cleansed

#### Object Definition
List of types of Functions that are associated to convention or group reservations: ie: Setup &amp; Teardown Charge
Exhibit Space Rental
Refrigerator Rental
Risers/Flipcharts
Magic Kingdom Tour
Saute Chef/Carver Charge
Ticket Sales
Massage
Golf
Hospitality Room
Bar Refresh
Package Bar
Breakfast, Lunch, Dinner
Business Center

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_fnc_typ_id & metadata_checksum combination.

#### Primary key
data_fnc_typ_id

#### Tags
    - object_name=fnc_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__fnc_typ_versioned %}

#### Object Name
fnc_typ_versioned

#### Object Definition
List of types of Functions that are associated to convention or group reservations: ie: Setup &amp; Teardown Charge
Exhibit Space Rental
Refrigerator Rental
Risers/Flipcharts
Magic Kingdom Tour
Saute Chef/Carver Charge
Ticket Sales
Massage
Golf
Hospitality Room
Bar Refresh
Package Bar
Breakfast, Lunch, Dinner
Business Center

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_fnc_typ_id & metadata_checksum combination.

#### Primary key
data_fnc_typ_id

#### Tags
    - object_name=fnc_typ
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}