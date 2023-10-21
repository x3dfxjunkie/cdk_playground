{% docs sil__intermediate__dreams__rooms_fulfillment__dvc_pt_pmt_ref_cleansed %}

#### Object Name
dvc_pt_pmt_ref_cleansed

#### Object Definition
If a reservation is booked using Disney Vacation Club points, this table is populated with a value that references the guest points account.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_dvc_pt_pmt_ref_id & metadata_checksum combination.

#### Primary key
data_dvc_pt_pmt_ref_id

#### Tags
    - object_name=dvc_pt_pmt_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__rooms_fulfillment__dvc_pt_pmt_ref_versioned %}

#### Object Name
dvc_pt_pmt_ref_versioned

#### Object Definition
If a reservation is booked using Disney Vacation Club points, this table is populated with a value that references the guest points account.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_dvc_pt_pmt_ref_id & metadata_checksum combination.

#### Primary key
data_dvc_pt_pmt_ref_id

#### Tags
    - object_name=dvc_pt_pmt_ref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}