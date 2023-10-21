{% docs sil__guest_experience__magic_band__magic_band_facility_transfer_current %}

Object Name
magic_band_facility_transfer_current

Object Definition
Fulfilled Magic Bands that have been located at a Disney Facility (confirmed by an entry in the inventory) can be transfered to an alternative facility. A transfer is captured at the individual band level and a delivery date is associated with each band to be transfered. When the band has been scanned at the destination location the inventory is updated with the new location of the band. A transfer is expected to contain many bands in the order of 100s a different transfer batch is identified by a common the source, destination and expected delivery date.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_facility_transfer_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}