{% docs sil__intermediate__dreams__entitlements__cpn_txn_t_cleansed %}

#### Table Name
cpn_txn_t_cleansed

#### Table Definition
This table ties the transaction type: TXN_TYP_NM
        SALE
        REV
        TRF
        with the coupon charge ID

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_cpn_chrg_id, data_orig_chrg_id, data_txn_id & metadata_checksum combination.

#### Primary key
data_cpn_chrg_id, data_orig_chrg_id, data_txn_id

#### Tags
    - table_name=cpn_txn_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__entitlements__cpn_txn_t_versioned %}

#### Table Name
cpn_txn_t_versioned

#### Table Definition
This table ties the transaction type: TXN_TYP_NM
        SALE
        REV
        TRF
        with the coupon charge ID

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_cpn_chrg_id, data_orig_chrg_id, data_txn_id & metadata_checksum combination.

#### Primary key
data_cpn_chrg_id, data_orig_chrg_id, data_txn_id

#### Tags
    - table_name=cpn_txn_t
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}