{% docs sil__guest_experience__magic_band__magic_band_status_activity_current %}

Object Name
magic_band_status_activity_current

Object Definition
The activity for status changes applied to a Request. Changes in Magic Band Request Status typically capture the process of locking a Request from customization prior to the Order creation and do not change after this point. In the case were an Order is cancelled before the being sent to fulfillment the status would change from not sent to fulfillment to cancelled before fulfillment to distinguish between and request that will one day become and order and one that will not.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_status_activity_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}