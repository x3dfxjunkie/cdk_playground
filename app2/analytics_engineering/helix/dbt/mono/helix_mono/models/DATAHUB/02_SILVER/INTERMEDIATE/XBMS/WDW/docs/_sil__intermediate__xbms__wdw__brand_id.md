{% docs sil__intermediate__xbms__wdw__brand_id_cleansed %}

#### Object Name
brand_id_cleansed

#### Object Definition
Reference table for magicband brand codes and their brand names. Such as Star Wars, Pixar, Marvel, Disney Parks, Animation, etc.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_brand_typ_id & metadata_checksum combination.

#### Primary key
data_brand_typ_id

#### Tags
    - object_name=brand_id
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__xbms__wdw__brand_id_versioned %}

#### Object Name
brand_id_versioned

#### Object Definition
Reference table for magicband brand codes and their brand names. Such as Star Wars, Pixar, Marvel, Disney Parks, Animation, etc.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_brand_typ_id & metadata_checksum combination.

#### Primary key
data_brand_typ_id

#### Tags
    - object_name=brand_id
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}