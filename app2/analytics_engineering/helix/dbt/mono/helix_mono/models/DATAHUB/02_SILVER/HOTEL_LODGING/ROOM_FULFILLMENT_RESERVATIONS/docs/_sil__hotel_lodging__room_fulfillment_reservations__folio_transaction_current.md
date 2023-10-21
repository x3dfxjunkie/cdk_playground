{% docs sil__hotel_lodging__room_fulfillment_reservations__folio_transaction_current %}

Object Name
folio_transaction_current

Object Definition
This table captures the datetime, folio type ie SALE, REC, RED, etc. and ties it to the payment item or the charge and what procedure occurred ie: CREATED, AFFECTED, etc.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=folio_transaction_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=room_fulfillment_reservations

{% enddocs %}