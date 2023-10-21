{% docs sil__intermediate__dreams__resource_inventory_management__dvc_rm_typ_xref_cleansed %}

#### Object Name
dvc_rm_typ_xref_cleansed

#### Object Definition
This table maps the Disney Vacation Club room type codes to the resource inventory room type codes

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_dvc_rm_typ_xref_id & metadata_checksum combination.

#### Primary key
data_dvc_rm_typ_xref_id

#### Tags
    - object_name=dvc_rm_typ_xref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__dreams__resource_inventory_management__dvc_rm_typ_xref_versioned %}

#### Object Name
dvc_rm_typ_xref_versioned

#### Object Definition
This table maps the Disney Vacation Club room type codes to the resource inventory room type codes

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_dvc_rm_typ_xref_id & metadata_checksum combination.

#### Primary key
data_dvc_rm_typ_xref_id

#### Tags
    - object_name=dvc_rm_typ_xref
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}