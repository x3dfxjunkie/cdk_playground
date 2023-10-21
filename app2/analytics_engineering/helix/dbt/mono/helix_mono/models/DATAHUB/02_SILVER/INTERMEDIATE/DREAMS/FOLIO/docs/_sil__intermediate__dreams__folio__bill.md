{% docs sil__intermediate__dreams__folio__bill_cleansed %}

#### Object Name
bill_cleansed

#### Object Definition
Billing codes that are associated to Conventions/Groups that determines who pays for what, the delegate or the Convention/Group

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_bill_id & metadata_checksum combination.

#### Primary key
data_bill_id

#### Tags
    - object_name=bill
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__bill_versioned %}

#### Object Name
bill_versioned

#### Object Definition
Billing codes that are associated to Conventions/Groups that determines who pays for what, the delegate or the Convention/Group

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_bill_id & metadata_checksum combination.

#### Primary key
data_bill_id

#### Tags
    - object_name=bill
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}