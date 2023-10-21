{% docs sil__hotel_lodging__room_fulfillment_reservations__reservation_history_current %}

Object Name
reservation_history_current

Object Definition
This table tracks the transactional procedures through history for travel components ie: book, modify, checkin, etc.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=reservation_history_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=room_fulfillment_reservations

{% enddocs %}