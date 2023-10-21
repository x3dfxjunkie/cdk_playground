{% docs sil__intermediate__dreams__price__chg_typ_t_cleansed %}

#### Object Name
chg_typ_t_cleansed

#### Object Definition
List of charge types: Sales Tax - Beaufort County (SC) - Merchandise, Communications Tax - Beaufort County (SC), Adjust for Discount, Sales Tax - Beaufort County (SC) - Food, Osceola County Accommodation Tax, Osceola County Tourist Development Tax, Indian River FL Tourist Development Tax, Anaheim Room Occupancy Tax, ATID Assessment, Indian River County Accommodation Tax, Accommodations Tax - Hawaii State, Orange County Tourist Development Tax, Orange County Sales Tax, Indian River County Sales Tax, South Carolina State Accommodation Tax, Sales Tax - Beaufort County (SC) - Liquor, Orange County California Sales Tax, Osceola County Sales Tax, Transportation Tax - Beaufort County (SC), Base, Sales Tax - Beaufort County (SC), Brevard County Sales Tax, Accommodations Tax - Honolulu County (HI), Reverse Original, Sales Tax - South Carolina State (not rooms), Cross County Tax Adjustment, Hilton Head City Accommodation Tax, Osceola County Sales Tax, Additional Adult, Orange County Accommodation Tax, Indian River Tourist Development Tax, Communications Tax - Osceola County (FL), California State Sales Tax, Deposit Requirement, General Excise Tax - Hawaii State, Communications Tax - Orange County (FL), Florida State Accommodations Tax, Tax, Discount, South Carolina State Sales Tax, Communications Tax - Indian River County (FL), City of Anaheim Sales Tax

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_chg_typ_nm & metadata_checksum combination.

#### Primary key
data_chg_typ_nm

#### Tags
    - object_name=chg_typ_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__chg_typ_t_versioned %}

#### Object Name
chg_typ_t_versioned

#### Object Definition
List of charge types: Sales Tax - Beaufort County (SC) - Merchandise, Communications Tax - Beaufort County (SC), Adjust for Discount, Sales Tax - Beaufort County (SC) - Food, Osceola County Accommodation Tax, Osceola County Tourist Development Tax, Indian River FL Tourist Development Tax, Anaheim Room Occupancy Tax, ATID Assessment, Indian River County Accommodation Tax, Accommodations Tax - Hawaii State, Orange County Tourist Development Tax, Orange County Sales Tax, Indian River County Sales Tax, South Carolina State Accommodation Tax, Sales Tax - Beaufort County (SC) - Liquor, Orange County California Sales Tax, Osceola County Sales Tax, Transportation Tax - Beaufort County (SC), Base, Sales Tax - Beaufort County (SC), Brevard County Sales Tax, Accommodations Tax - Honolulu County (HI), Reverse Original, Sales Tax - South Carolina State (not rooms), Cross County Tax Adjustment, Hilton Head City Accommodation Tax, Osceola County Sales Tax, Additional Adult, Orange County Accommodation Tax, Indian River Tourist Development Tax, Communications Tax - Osceola County (FL), California State Sales Tax, Deposit Requirement, General Excise Tax - Hawaii State, Communications Tax - Orange County (FL), Florida State Accommodations Tax, Tax, Discount, South Carolina State Sales Tax, Communications Tax - Indian River County (FL), City of Anaheim Sales Tax

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_chg_typ_nm & metadata_checksum combination.

#### Primary key
data_chg_typ_nm

#### Tags
    - object_name=chg_typ_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}