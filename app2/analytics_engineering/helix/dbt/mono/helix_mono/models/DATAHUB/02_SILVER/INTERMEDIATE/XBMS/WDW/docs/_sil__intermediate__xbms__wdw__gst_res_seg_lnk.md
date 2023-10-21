{% docs sil__intermediate__xbms__wdw__gst_res_seg_lnk_cleansed %}

#### Object Name
gst_res_seg_lnk_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_gst_res_seg_lnk_id & metadata_checksum combination.

#### Primary key
data_gst_res_seg_lnk_id

#### Tags
    - object_name=gst_res_seg_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__gst_res_seg_lnk_versioned %}

#### Object Name
gst_res_seg_lnk_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_gst_res_seg_lnk_id & metadata_checksum combination.

#### Primary key
data_gst_res_seg_lnk_id

#### Tags
    - object_name=gst_res_seg_lnk
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}