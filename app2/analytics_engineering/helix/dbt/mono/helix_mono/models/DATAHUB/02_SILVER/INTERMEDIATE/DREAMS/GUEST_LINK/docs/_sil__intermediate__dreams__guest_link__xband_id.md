{% docs sil__intermediate__dreams__guest_link__xband_id_cleansed %}

#### Object Name
xband_id_cleansed

#### Object Definition
This table ties together the experience media ID and the Magic Band ID value: XBAND_ID_TYP_NM
        PUBLIC_LONG_RANGE_ID
        PUBLIC_SHORT_RANGE_ID
        XBMS_XBAND_ID
        VISUAL_ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_exprnc_media_id, data_xband_id_typ_nm, data_xband_id_vl & metadata_checksum combination.

#### Primary key
data_exprnc_media_id, data_xband_id_typ_nm, data_xband_id_vl

#### Tags
    - object_name=xband_id
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__guest_link__xband_id_versioned %}

#### Object Name
xband_id_versioned

#### Object Definition
This table ties together the experience media ID and the Magic Band ID value: XBAND_ID_TYP_NM
        PUBLIC_LONG_RANGE_ID
        PUBLIC_SHORT_RANGE_ID
        XBMS_XBAND_ID
        VISUAL_ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_exprnc_media_id, data_xband_id_typ_nm, data_xband_id_vl & metadata_checksum combination.

#### Primary key
data_exprnc_media_id, data_xband_id_typ_nm, data_xband_id_vl

#### Tags
    - object_name=xband_id
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}