{% docs sil__hotel_lodging__inventory__business_organization_current %}

Object Name
business_organization_current

Object Definition
This table ties together the campus: WDW, DLR, PAC(Aulani) with the related time zone and the related businesses Scheduled Events, Resort Operations, DRC(Disney Central call center)

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=business_organization_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=inventory

{% enddocs %}