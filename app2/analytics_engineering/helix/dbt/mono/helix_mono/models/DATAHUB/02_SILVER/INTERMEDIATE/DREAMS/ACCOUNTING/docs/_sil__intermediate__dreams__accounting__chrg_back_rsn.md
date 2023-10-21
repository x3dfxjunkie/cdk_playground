{% docs sil__intermediate__dreams__accounting__chrg_back_rsn_cleansed %}

#### Object Name
chrg_back_rsn_cleansed

#### Object Definition
List of the reasons a charge back would occur this list isn&#39;t complete: Poor Service Bell Services
Rehab
Tickets-Lost or Stolen
Noise
Poor Service Housekeeping
Water or Pipe Break
Goodwill or Illness
Poor Service Engineering
Package Handling Fee
Poor Service
No Show Arrival
Poor Service Valet
Poor Experience-Parks

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chrg_back_rsn_id & metadata_checksum combination.

#### Primary key
data_chrg_back_rsn_id

#### Tags
    - object_name=chrg_back_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__chrg_back_rsn_versioned %}

#### Object Name
chrg_back_rsn_versioned

#### Object Definition
List of the reasons a charge back would occur this list isn&#39;t complete: Poor Service Bell Services
Rehab
Tickets-Lost or Stolen
Noise
Poor Service Housekeeping
Water or Pipe Break
Goodwill or Illness
Poor Service Engineering
Package Handling Fee
Poor Service
No Show Arrival
Poor Service Valet
Poor Experience-Parks

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chrg_back_rsn_id & metadata_checksum combination.

#### Primary key
data_chrg_back_rsn_id

#### Tags
    - object_name=chrg_back_rsn
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}