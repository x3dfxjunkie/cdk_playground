{% docs sil__guest_experience__magic_band__magic_band_current %}

Object Name
magic_band_current

Object Definition
AKA Experience Band. Refers to the wrist band or any other form factor that will carry an RFID chip.  All Bands have a color which is assigned at the time the entitlement for a Band is known (prior to the Band fulfillment). A Magic (Experience) Band which is not fulfilled to meet a specific Guest's entitlement for an Experience Band will not be immediately associated with a Guest. A band has an Order which is a Guest Request for a set of Experience Bands that have been (or are about to be) sent to fulfillment. The life cycle of an experience band transitions from a Request to an Order when the specification for the Customized Band and the intended recipient for the bands is submitted to the Fulfillment House. An Order has an status associated status used to describe where the order is in the fulfillment process. The shipping carrier is determined by the fulfillment house during fulfilment and the link between the order and the shipping carrier is made on receipt of the fulfillment report from the fulfillment house. An Experience Band Request notifies the Experience Band Management System of a need to fulfill an entitlement for an Experience Band.  The Request is created to capture the collection of Customized Bands, the Recipient and how the bands should be packaged when shipped to the recipient. The band is shipped in a package. Where the number of Bands ordered exceeds the capacity of a single Out Of Box Experience ("OOBE") there will be multiple Packages. The Packages are assigned a sequence within the shipment captured in the Package Sequence Number.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}