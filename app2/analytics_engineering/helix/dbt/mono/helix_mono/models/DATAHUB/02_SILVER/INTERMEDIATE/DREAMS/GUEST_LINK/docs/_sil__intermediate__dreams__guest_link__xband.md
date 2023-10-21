{% docs sil__intermediate__dreams__guest_link__xband_cleansed %}

#### Object Name
xband_cleansed

#### Object Definition
This table ties the following attributes and or IDs to the Experience Media ID: XBAND_STS_NM
ACTIVE
INACTIVE
VOID
XBAND_SEC_STS_NM
BUSINESS_NEED
BUSINESS_NEEDS_CHECKED_OUT
DAMAGED
etc., manufacturer User ID, Experience Card ID, or HF_SECURE_XBAND_ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_exprnc_media_id & metadata_checksum combination.

#### Primary key
data_exprnc_media_id

#### Tags
    - object_name=xband
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest_link__xband_versioned %}

#### Object Name
xband_versioned

#### Object Definition
This table ties the following attributes and or IDs to the Experience Media ID: XBAND_STS_NM
ACTIVE
INACTIVE
VOID
XBAND_SEC_STS_NM
BUSINESS_NEED
BUSINESS_NEEDS_CHECKED_OUT
DAMAGED
etc., manufacturer User ID, Experience Card ID, or HF_SECURE_XBAND_ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_exprnc_media_id & metadata_checksum combination.

#### Primary key
data_exprnc_media_id

#### Tags
    - object_name=xband
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}