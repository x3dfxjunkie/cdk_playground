{% docs sil__hotel_lodging__inventory__rooms_current %}

Object Name
rooms_current

Object Definition
This table provides the tie between the reservable resource(room category) to an actual physical room and to any connecting rooms

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=rooms_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=inventory

{% enddocs %}