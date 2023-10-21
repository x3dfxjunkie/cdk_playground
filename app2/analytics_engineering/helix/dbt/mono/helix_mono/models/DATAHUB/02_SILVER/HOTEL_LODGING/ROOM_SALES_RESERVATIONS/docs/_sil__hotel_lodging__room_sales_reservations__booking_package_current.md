{% docs sil__hotel_lodging__room_sales_reservations__booking_package_current %}

Object Name
booking_package_current

Object Definition
The booking of a travel package under a specific travel reservation. While packages are available to be booked under many reservations, multiple packages may be booked within a single travel reservation.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=booking_package_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=room_sales_reservations

{% enddocs %}