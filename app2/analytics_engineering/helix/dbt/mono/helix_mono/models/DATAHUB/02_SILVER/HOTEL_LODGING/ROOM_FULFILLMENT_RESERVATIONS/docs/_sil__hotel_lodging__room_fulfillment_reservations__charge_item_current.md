{% docs sil__hotel_lodging__room_fulfillment_reservations__charge_item_current %}

Object Name
charge_item_current

Object Definition
this table holds charge item level amounts, there is a Base and Additional items consisting of different taxes, discount(this is a terrible name it's not at all correct) additional adult charge, base etc. Not all charges will have all item types but there will always be a base item type.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=charge_item_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=room_fulfillment_reservations

{% enddocs %}