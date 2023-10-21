{% docs sil__hotel_lodging__room_fulfillment_reservations__reservations_current %}

Object Name
reservations_current

Object Definition
This table contains information related to Room reservations, including arrival and departure date, status, sales and communication channels as well as the IDs that tie to more information regarding travel agencies, groups, wholesalers, etc.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=reservations_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=room_fulfillment_reservations

{% enddocs %}