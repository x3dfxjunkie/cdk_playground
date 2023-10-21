{% docs sil__intermediate__dreams__accounting__sap_bus_area_cleansed %}

#### Object Name
sap_bus_area_cleansed

#### Object Definition
SAP Business Area names associated to SAP Business Area Codes

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_sap_bus_area_cd & metadata_checksum combination.

#### Primary key
data_sap_bus_area_cd

#### Tags
    - object_name=sap_bus_area
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__accounting__sap_bus_area_versioned %}

#### Object Name
sap_bus_area_versioned

#### Object Definition
SAP Business Area names associated to SAP Business Area Codes

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_sap_bus_area_cd & metadata_checksum combination.

#### Primary key
data_sap_bus_area_cd

#### Tags
    - object_name=sap_bus_area
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}