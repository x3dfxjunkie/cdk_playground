{% docs sil__guest_experience__magic_band__magic_band_order_status_activity_current %}

Object Name
magic_band_order_status_activity_current

Object Definition
The activity for status changes applied to a Magic Band Order. The changes may progress through until an Order has been shipped to the recipient. An Order may be recorded as cancelled before or even after shipping to the recipient.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_order_status_activity_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}