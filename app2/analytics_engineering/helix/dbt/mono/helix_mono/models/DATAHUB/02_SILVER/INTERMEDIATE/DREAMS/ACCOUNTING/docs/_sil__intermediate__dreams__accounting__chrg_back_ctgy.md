{% docs sil__intermediate__dreams__accounting__chrg_back_ctgy_cleansed %}

#### Object Name
chrg_back_ctgy_cleansed

#### Object Definition
Provides the categories that can be charged back:
Disney&#39;s Magical Express
Tickets
Comp Tickets
Rollaway Bed
Resort Service Inconvenience
Refrigerator Rental
Self Parking Fee
Phone - Long Distance
Phone - Local
Pager Rental
Laundry
Room Rate Adjustment
Phone - 800/Toll Free
a la carte
Minibars
Newspaper
Room Defect
POS Adjustment
Transportation

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrg_back_ctgy_id & metadata_checksum combination.

#### Primary key
data_chrg_back_ctgy_id

#### Tags
    - object_name=chrg_back_ctgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__chrg_back_ctgy_versioned %}

#### Object Name
chrg_back_ctgy_versioned

#### Object Definition
Provides the categories that can be charged back:
Disney&#39;s Magical Express
Tickets
Comp Tickets
Rollaway Bed
Resort Service Inconvenience
Refrigerator Rental
Self Parking Fee
Phone - Long Distance
Phone - Local
Pager Rental
Laundry
Room Rate Adjustment
Phone - 800/Toll Free
a la carte
Minibars
Newspaper
Room Defect
POS Adjustment
Transportation

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrg_back_ctgy_id & metadata_checksum combination.

#### Primary key
data_chrg_back_ctgy_id

#### Tags
    - object_name=chrg_back_ctgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}