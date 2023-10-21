{% docs sil__hotel_lodging__inventory__room_assignment_history_current %}

Object Name
room_assignment_history_current

Object Definition
This table provides the history of the physical rooms in a hotel, by multiple statuses, actions, travel with IDs and group IDs

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=room_assignment_history_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=inventory

{% enddocs %}