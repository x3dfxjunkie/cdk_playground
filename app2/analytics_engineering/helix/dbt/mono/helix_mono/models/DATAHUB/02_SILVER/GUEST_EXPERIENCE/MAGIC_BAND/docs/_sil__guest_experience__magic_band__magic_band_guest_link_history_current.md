{% docs sil__guest_experience__magic_band__magic_band_guest_link_history_current %}

Object Name
magic_band_guest_link_history_current

Object Definition
When Guests have more than one guest identifier in the source, the source will merge them into one link id so that it can uniquely identify a Guest.  The Primary Link ID is the one that the source will use and the prior will no longer be used in the source.  We can know the history of all link IDs in this table as they all roll up to the same ID.  For example, over time, Guest Pat has had 10 link IDs.  By querying this table, we will be able to find the one link ID which is primarily active in the source system for Pat.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_guest_link_history_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}