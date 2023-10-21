{% docs sil__guest_experience__magic_band__magic_band_order_current %}

Object Name
magic_band_order_current

Object Definition
An Order is a Guest Request for a set of Magic Bands that have been (or are about to be) sent to fulfillment. The life cycle of a magic band transitions from a Request to an Order when the specification for the Customized Band and the intended recipient for the bands is submitted to the Fulfillment House. An Order has an status associated status used to describe where the order is in the fulfillment process. The shipping carrier is determined by the fulfillment house during fulfillment and the link between the order and the shipping carrier is made on receipt of the fulfillment report from the fulfillment house.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_order_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}