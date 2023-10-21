{% docs sil__intermediate__dreams__rooms_fulfillment__trvl_sts_cleansed %}

#### Object Name
trvl_sts_cleansed

#### Object Definition
List of travel statuses: TRVL_STS_NM, Past Visit, Checked In, Auto Arrived, Arrived, Not Arrived, Checking In, DF Checked Out, Early Check Out, Auto Cancelled, No Show, Cancelled, Booked

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_trvl_sts_nm & metadata_checksum combination.

#### Primary key
data_trvl_sts_nm

#### Tags
    - object_name=trvl_sts
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__trvl_sts_versioned %}

#### Object Name
trvl_sts_versioned

#### Object Definition
List of travel statuses: TRVL_STS_NM, Past Visit, Checked In, Auto Arrived, Arrived, Not Arrived, Checking In, DF Checked Out, Early Check Out, Auto Cancelled, No Show, Cancelled, Booked

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_trvl_sts_nm & metadata_checksum combination.

#### Primary key
data_trvl_sts_nm

#### Tags
    - object_name=trvl_sts
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}