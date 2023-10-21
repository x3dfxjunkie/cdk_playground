{% docs sil__hotel_lodging__inventory__component_external_reference_current %}

Object Name
component_external_reference_current

Object Definition
This table provide ties the room sequence to the resort sequence of the room rack(physical rooms). It's many to 1 to the reservable resource ID based on Sequence Name, which is not versioned. Need Business rules to determine which sequence name to use.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=component_external_reference_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=inventory

{% enddocs %}