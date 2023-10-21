{% docs sil__intermediate__dreams__accounting__acct_dstr_chan_mtx_cleansed %}

#### Object Name
acct_dstr_chan_mtx_cleansed

#### Object Definition
This field maps reservation sales and communication channels to a SAP channel

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acct_dstr_chan_mtrx_id & metadata_checksum combination.

#### Primary key
data_acct_dstr_chan_mtrx_id

#### Tags
    - object_name=acct_dstr_chan_mtx
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__acct_dstr_chan_mtx_versioned %}

#### Object Name
acct_dstr_chan_mtx_versioned

#### Object Definition
This field maps reservation sales and communication channels to a SAP channel

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acct_dstr_chan_mtrx_id & metadata_checksum combination.

#### Primary key
data_acct_dstr_chan_mtrx_id

#### Tags
    - object_name=acct_dstr_chan_mtx
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}