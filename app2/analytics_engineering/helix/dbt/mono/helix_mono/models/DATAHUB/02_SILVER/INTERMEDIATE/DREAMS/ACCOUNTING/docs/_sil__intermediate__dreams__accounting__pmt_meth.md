{% docs sil__intermediate__dreams__accounting__pmt_meth_cleansed %}

#### Object Name
pmt_meth_cleansed

#### Object Definition
Information associated to a Payment Method type: Bill to A/R, CreditCard, Hotel Charges, Entitlements, DisneyRewardCard, PaidOut, Voucher, Check, Cash, Redeem, Settle to Folio, System, PaymentSystem, Direct Bill, PrePaidCard, RSR, Non-Folio Refunds

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_pmt_meth_id & metadata_checksum combination.

#### Primary key
data_pmt_meth_id

#### Tags
    - object_name=pmt_meth
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__pmt_meth_versioned %}

#### Object Name
pmt_meth_versioned

#### Object Definition
Information associated to a Payment Method type: Bill to A/R, CreditCard, Hotel Charges, Entitlements, DisneyRewardCard, PaidOut, Voucher, Check, Cash, Redeem, Settle to Folio, System, PaymentSystem, Direct Bill, PrePaidCard, RSR, Non-Folio Refunds

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_pmt_meth_id & metadata_checksum combination.

#### Primary key
data_pmt_meth_id

#### Tags
    - object_name=pmt_meth
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}