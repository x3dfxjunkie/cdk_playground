{% docs sil__intermediate__dreams__dining__acm_cmpnt_chrnlgy_cleansed %}

#### Object Name
acm_cmpnt_chrnlgy_cleansed

#### Object Definition
This table has the estimated time of arrival, depature, etc for the accommodation travel component provided by multiple sources. IE: OLCI- online check in, SECURITY_GATE, etc

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acm_cmpnt_chrnlgy_id & metadata_checksum combination.

#### Primary key
data_acm_cmpnt_chrnlgy_id

#### Tags
    - object_name=acm_cmpnt_chrnlgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__dining__acm_cmpnt_chrnlgy_versioned %}

#### Object Name
acm_cmpnt_chrnlgy_versioned

#### Object Definition
This table has the estimated time of arrival, depature, etc for the accommodation travel component provided by multiple sources. IE: OLCI- online check in, SECURITY_GATE, etc

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acm_cmpnt_chrnlgy_id & metadata_checksum combination.

#### Primary key
data_acm_cmpnt_chrnlgy_id

#### Tags
    - object_name=acm_cmpnt_chrnlgy
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}