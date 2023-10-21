{% docs sil__intermediate__dreams__folio__folio_chkot_opt_cleansed %}

#### Object Name
folio_chkot_opt_cleansed

#### Object Definition
This table holds the manner in which the guest would like to receive their Folio at Check out:  CHKOT_OPT_TYP_NM( EXPRESS_CHECK_OUT, PRINT, EMAIL)

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_folio_chkot_opt_id & metadata_checksum combination.

#### Primary key
data_folio_chkot_opt_id

#### Tags
    - object_name=folio_chkot_opt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__folio__folio_chkot_opt_versioned %}

#### Object Name
folio_chkot_opt_versioned

#### Object Definition
This table holds the manner in which the guest would like to receive their Folio at Check out:  CHKOT_OPT_TYP_NM( EXPRESS_CHECK_OUT, PRINT, EMAIL)

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_folio_chkot_opt_id & metadata_checksum combination.

#### Primary key
data_folio_chkot_opt_id

#### Tags
    - object_name=folio_chkot_opt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}