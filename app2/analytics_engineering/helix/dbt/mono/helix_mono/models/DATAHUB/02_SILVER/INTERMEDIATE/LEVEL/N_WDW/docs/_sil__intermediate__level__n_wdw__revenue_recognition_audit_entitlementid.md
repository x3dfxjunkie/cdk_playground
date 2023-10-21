{% docs sil__intermediate__level__n_wdw__revenue_recognition_audit_entitlementid_cleansed %}

#### Object Name
revenue_recognition_audit_entitlementid_cleansed

#### Object Definition
Table containing the recognized revenue and the corresponding entitlement id and transaction id.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_entitlement_id, data_transaction_id & metadata_checksum combination.

#### Primary key
data_entitlement_id, data_transaction_id

#### Tags
    - object_name=revenue_recognition_audit_entitlementid
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__level__n_wdw__revenue_recognition_audit_entitlementid_versioned %}

#### Object Name
revenue_recognition_audit_entitlementid_versioned

#### Object Definition
Table containing the recognized revenue and the corresponding entitlement id and transaction id.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_entitlement_id, data_transaction_id & metadata_checksum combination.

#### Primary key
data_entitlement_id, data_transaction_id

#### Tags
    - object_name=revenue_recognition_audit_entitlementid
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}