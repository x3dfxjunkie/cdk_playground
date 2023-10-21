{% docs sil__intermediate__dreams__rooms_fulfillment__adm_cmpnt_enttl_cleansed %}

#### Object Name
adm_cmpnt_enttl_cleansed

#### Object Definition
When a room reservation includes Admissions to the park, the ticket is fulfilled in Snapp - the system of record for Tickets. It contains barcode, magnetic strip and serial number value - which is the Ticket identifier in Snapp. Any updates to the ticket after that will occur in Snapp

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_adm_enttl_id & metadata_checksum combination.

#### Primary key
data_adm_enttl_id

#### Tags
    - object_name=adm_cmpnt_enttl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__adm_cmpnt_enttl_versioned %}

#### Object Name
adm_cmpnt_enttl_versioned

#### Object Definition
When a room reservation includes Admissions to the park, the ticket is fulfilled in Snapp - the system of record for Tickets. It contains barcode, magnetic strip and serial number value - which is the Ticket identifier in Snapp. Any updates to the ticket after that will occur in Snapp

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_adm_enttl_id & metadata_checksum combination.

#### Primary key
data_adm_enttl_id

#### Tags
    - object_name=adm_cmpnt_enttl
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}