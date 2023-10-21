{% docs sil__guest_experience__magic_band__magic_band_entitlement_guest_product_current %}

Object Name
magic_band_entitlement_guest_product_current

Object Definition
For each Magic Band entitlement, which is driven by a level, this identifies a default product assigned to that entitlement, as well as a list of Magic Band products that are available to that entitlement for a particular Guest.  When the Guest books a reservation, the list of available Magic Band products under the entitlement are displayed to them on their screen for choosing a product.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_entitlement_guest_product_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}