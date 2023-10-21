{% docs sil__intermediate__dreams__accounting__pmt_meth_nb_rnge_cleansed %}

#### Object Name
pmt_meth_nb_rnge_cleansed

#### Object Definition
Payment Method tied to a starting number and ending number for a specific time frame

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pmt_meth_nb_rnge_id & metadata_checksum combination.

#### Primary key
data_pmt_meth_nb_rnge_id

#### Tags
    - object_name=pmt_meth_nb_rnge
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__pmt_meth_nb_rnge_versioned %}

#### Object Name
pmt_meth_nb_rnge_versioned

#### Object Definition
Payment Method tied to a starting number and ending number for a specific time frame

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pmt_meth_nb_rnge_id & metadata_checksum combination.

#### Primary key
data_pmt_meth_nb_rnge_id

#### Tags
    - object_name=pmt_meth_nb_rnge
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}