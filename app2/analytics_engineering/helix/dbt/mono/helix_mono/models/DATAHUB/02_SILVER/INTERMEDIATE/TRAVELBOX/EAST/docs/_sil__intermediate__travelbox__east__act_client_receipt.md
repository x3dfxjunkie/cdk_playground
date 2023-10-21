{% docs sil__intermediate__travelbox__east__act_client_receipt_cleansed %}

#### Object Name
act_client_receipt_cleansed

#### Object Definition
This table is used to store information of Client Receipt Details. The values are saved when proceeding in the
following path. In Accounts Client go to &#39;Receipts-&gt;Single Receipts&#39;. Then &#39;Search&#39; for the bookings to add receipts.
then select the booking to add the receipt from the &#39;Select booking/s Grid&#39;, then click&#39;Add New Receipt&#39;. Then
select any payment type from the &#39;Type/Amount&#39; dropdown and click &#39;Add&#39; button from the dropdown  and
then &#39;Save&#39;. And also values are saved when proceeding in the &#39;payment&#39; node in Reservetion Manger.Then click
&#39;Payment&#39; button and add the payment in &#39;Payment Detail Panel&#39;.

#### Business Rules
This is a cleansed and deduplicated version of the bronze table inside the silver intermediate layer.

#### Granularity
One record per data_booking_id, data_receipt_index & metadata_checksum combination.

#### Primary key
data_booking_id, data_receipt_index

#### Tags
    - object_name=act_client_receipt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_cleansed

{% enddocs %}

{% docs sil__intermediate__travelbox__east__act_client_receipt_versioned %}

#### Object Name
act_client_receipt_versioned

#### Object Definition
This table is used to store information of Client Receipt Details. The values are saved when proceeding in the
following path. In Accounts Client go to &#39;Receipts-&gt;Single Receipts&#39;. Then &#39;Search&#39; for the bookings to add receipts.
then select the booking to add the receipt from the &#39;Select booking/s Grid&#39;, then click&#39;Add New Receipt&#39;. Then
select any payment type from the &#39;Type/Amount&#39; dropdown and click &#39;Add&#39; button from the dropdown  and
then &#39;Save&#39;. And also values are saved when proceeding in the &#39;payment&#39; node in Reservetion Manger.Then click
&#39;Payment&#39; button and add the payment in &#39;Payment Detail Panel&#39;.

#### Business Rules
This table is built on the top of the cleansed table. In addition to the cleansed table fields, it contains the versioning fields also.

#### Granularity
One record per data_booking_id, data_receipt_index & metadata_checksum combination.

#### Primary key
data_booking_id, data_receipt_index

#### Tags
    - object_name=act_client_receipt
    - layer=silver_intermediate
    - sub_layer=silver_intermediate_versioned

{% enddocs %}