{% docs sil__intermediate__dreams__guest_link__exprnc_media_cleansed %}

#### Object Name
exprnc_media_cleansed

#### Object Definition
This table associates the experience media ID with the guest link ID by Media Type: EXPRNC_MEDIA_TYP_NM
        XBAND
        MAG_PLUS_RFID_CARD
        RFID_ONLY_CARD

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_exprnc_media_id & metadata_checksum combination.

#### Primary key
data_exprnc_media_id

#### Tags
    - object_name=exprnc_media
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest_link__exprnc_media_versioned %}

#### Object Name
exprnc_media_versioned

#### Object Definition
This table associates the experience media ID with the guest link ID by Media Type: EXPRNC_MEDIA_TYP_NM
        XBAND
        MAG_PLUS_RFID_CARD
        RFID_ONLY_CARD

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_exprnc_media_id & metadata_checksum combination.

#### Primary key
data_exprnc_media_id

#### Tags
    - object_name=exprnc_media
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}