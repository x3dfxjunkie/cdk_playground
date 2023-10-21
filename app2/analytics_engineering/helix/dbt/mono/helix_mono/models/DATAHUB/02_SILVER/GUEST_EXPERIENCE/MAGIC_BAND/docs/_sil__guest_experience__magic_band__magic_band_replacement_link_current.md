{% docs sil__guest_experience__magic_band__magic_band_replacement_link_current %}

Object Name
magic_band_replacement_link_current

Object Definition
When a Magic Band is replaced with another band the two bands may be linked. This provides a means to report on a bands history at the level of a guests experience with a band beyond the lifecycle of an individual band. The reason for replacement is tracked using the status of the Parent band or the status of the associated Request or Order. The mechanism used for replacement is tracked from the Magic Band Replacement Linkage.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=magic_band_replacement_link_current
- layer=silver_final
- domain=guest_experience
- sub_domain=magic_band

{% enddocs %}