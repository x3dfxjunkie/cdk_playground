{% docs sil__hotel_lodging__room_fulfillment_reservations__payment_current %}

Object Name
payment_current

Object Definition
Payment table contains all different types of payments made for reservations, pre-paid events/dining, folio settlement, etc

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=payment_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=room_fulfillment_reservations

{% enddocs %}