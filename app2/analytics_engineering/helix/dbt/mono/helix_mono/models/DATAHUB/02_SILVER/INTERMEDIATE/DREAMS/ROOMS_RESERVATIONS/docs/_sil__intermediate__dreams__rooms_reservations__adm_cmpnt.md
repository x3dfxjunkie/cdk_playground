{% docs sil__intermediate__dreams__rooms_reservations__adm_cmpnt_cleansed %}

#### Object Name
adm_cmpnt_cleansed

#### Object Definition
When a reservation has admission components included, this table provides the enterprise Ticket Product Code that connects ticket product information across multiple applications. It also contains the tickets validity start and end dates which is a key attribute for date based tickets

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_adm_tc_id & metadata_checksum combination.

#### Primary key
data_adm_tc_id

#### Tags
    - object_name=adm_cmpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_reservations__adm_cmpnt_versioned %}

#### Object Name
adm_cmpnt_versioned

#### Object Definition
When a reservation has admission components included, this table provides the enterprise Ticket Product Code that connects ticket product information across multiple applications. It also contains the tickets validity start and end dates which is a key attribute for date based tickets

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_adm_tc_id & metadata_checksum combination.

#### Primary key
data_adm_tc_id

#### Tags
    - object_name=adm_cmpnt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}