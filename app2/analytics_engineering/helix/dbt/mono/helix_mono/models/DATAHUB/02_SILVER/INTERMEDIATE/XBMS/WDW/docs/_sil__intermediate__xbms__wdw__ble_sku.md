{% docs sil__intermediate__xbms__wdw__ble_sku_cleansed %}

#### Object Name
ble_sku_cleansed

#### Object Definition
Reference table for SKU IDs and their corresponding product ID and group information.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_ble_sku_id & metadata_checksum combination.

#### Primary key
data_ble_sku_id

#### Tags
    - object_name=ble_sku
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__ble_sku_versioned %}

#### Object Name
ble_sku_versioned

#### Object Definition
Reference table for SKU IDs and their corresponding product ID and group information.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_ble_sku_id & metadata_checksum combination.

#### Primary key
data_ble_sku_id

#### Tags
    - object_name=ble_sku
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}