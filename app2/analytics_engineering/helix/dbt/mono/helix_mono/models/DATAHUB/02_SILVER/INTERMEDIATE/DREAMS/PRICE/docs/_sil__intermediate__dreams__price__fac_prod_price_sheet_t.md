{% docs sil__intermediate__dreams__price__fac_prod_price_sheet_t_cleansed %}

#### Object Name
fac_prod_price_sheet_t_cleansed

#### Object Definition
Associates a Price Sheet to Products by Facility - Resort specific products: WDW Rollaway Bed Rental, Self Parking Fees at Aulani (Hawaii), Refrigerator, Pet Fee, Internet- Wireless Internet Access (WiFi), Internet - High Speed Internet Access (HSIA), Hawaii Accom Tax-V6-Hotel Room-Standard, Hawaii Accom Tax-Honolulu County (HI)-V6-Hotel Room-Standard, DVC Member Towel Package, DVC Member Shampoo and Conditioner, DVC Member Laundry Detergent, DVC Member Coffee Package, DVC Member - Room Change Service, DVC Housekeeping - Trash and Towel Service, DVC Housekeeping - Full Cleaning Service, Areobed Rental - Aulani, Aerobed Rental - WDW, Aerobed Rental - Vero Beach, Aerobed Rental - Hilton Head, Accommodations Tax DVC - Honolulu County (HI)- 6S - Deluxe Studio - Poolside Gardens View, Accommodations Tax DVC - Honolulu County (HI) - 6A - Deluxe Studio - Ocean View, Accommodations Tax DVC - Hawaii State - 6S - Deluxe Studio - Poolside Gardens View, Accommodation Tax DVC - Honolulu County (HI)- 6Y - Dedicated Two Bedroom Villa - Standard View, Accommodation Tax DVC - Honolulu County (HI)- 6W - Deluxe Studio - Standard View, Accommodation Tax DVC - Honolulu County (HI)- 6V - Grand Villa - Stand

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_fac_prod_price_sheet_id & metadata_checksum combination.

#### Primary key
data_fac_prod_price_sheet_id

#### Tags
    - object_name=fac_prod_price_sheet_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__price__fac_prod_price_sheet_t_versioned %}

#### Object Name
fac_prod_price_sheet_t_versioned

#### Object Definition
Associates a Price Sheet to Products by Facility - Resort specific products: WDW Rollaway Bed Rental, Self Parking Fees at Aulani (Hawaii), Refrigerator, Pet Fee, Internet- Wireless Internet Access (WiFi), Internet - High Speed Internet Access (HSIA), Hawaii Accom Tax-V6-Hotel Room-Standard, Hawaii Accom Tax-Honolulu County (HI)-V6-Hotel Room-Standard, DVC Member Towel Package, DVC Member Shampoo and Conditioner, DVC Member Laundry Detergent, DVC Member Coffee Package, DVC Member - Room Change Service, DVC Housekeeping - Trash and Towel Service, DVC Housekeeping - Full Cleaning Service, Areobed Rental - Aulani, Aerobed Rental - WDW, Aerobed Rental - Vero Beach, Aerobed Rental - Hilton Head, Accommodations Tax DVC - Honolulu County (HI)- 6S - Deluxe Studio - Poolside Gardens View, Accommodations Tax DVC - Honolulu County (HI) - 6A - Deluxe Studio - Ocean View, Accommodations Tax DVC - Hawaii State - 6S - Deluxe Studio - Poolside Gardens View, Accommodation Tax DVC - Honolulu County (HI)- 6Y - Dedicated Two Bedroom Villa - Standard View, Accommodation Tax DVC - Honolulu County (HI)- 6W - Deluxe Studio - Standard View, Accommodation Tax DVC - Honolulu County (HI)- 6V - Grand Villa - Stand

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_fac_prod_price_sheet_id & metadata_checksum combination.

#### Primary key
data_fac_prod_price_sheet_id

#### Tags
    - object_name=fac_prod_price_sheet_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}