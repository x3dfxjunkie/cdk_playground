{% docs sil__guest_experience__magic_band__magic_band_vendor_inventory_current %}

Object Name
magic_band_vendor_inventory_current

Object Definition
Information about xBand stock levels at a vendor (manufacturer or distubutor) and parameters such as the point stock should be re-orderd. Vendor inventory items have an on hand count which records how many bands are available to fulfill an order for bands to a facility (park or resort). Resorts do not track bands available for fulfillment as they are the end destination for fulfillment

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_vendor_inventory_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}