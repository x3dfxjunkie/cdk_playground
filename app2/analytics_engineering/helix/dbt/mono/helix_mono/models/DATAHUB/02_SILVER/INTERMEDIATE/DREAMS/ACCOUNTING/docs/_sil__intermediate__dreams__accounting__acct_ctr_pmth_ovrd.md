{% docs sil__intermediate__dreams__accounting__acct_ctr_pmth_ovrd_cleansed %}

#### Object Name
acct_ctr_pmth_ovrd_cleansed

#### Object Definition


#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_acct_ctr_pmt_meth_id, data_ovrd_rfnd_pmt_meth_id & metadata_checksum combination.

#### Primary key
data_acct_ctr_pmt_meth_id, data_ovrd_rfnd_pmt_meth_id

#### Tags
    - object_name=acct_ctr_pmth_ovrd
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__acct_ctr_pmth_ovrd_versioned %}

#### Object Name
acct_ctr_pmth_ovrd_versioned

#### Object Definition


#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_acct_ctr_pmt_meth_id, data_ovrd_rfnd_pmt_meth_id & metadata_checksum combination.

#### Primary key
data_acct_ctr_pmt_meth_id, data_ovrd_rfnd_pmt_meth_id

#### Tags
    - object_name=acct_ctr_pmth_ovrd
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}