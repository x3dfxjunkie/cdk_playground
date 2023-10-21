{% docs sil__hotel_lodging__room_sales_reservations__payment_receipt_current %}

Object Name
payment_receipt_current

Object Definition
Payments made for Travel Reservations between Walt Disney Travel Company and a Client. Each record represents either a Payment received from a Client or a payment refunded back to a Client. Each Payment is made using a single Payment Method and Receipt Type.

Business Rules
This is a silver table generated using the silver intermediate tables as source by considering the latest data.

Granularity

Primary key

Tags
- object_name=payment_receipt_current
- layer=silver_final
- domain=hotel_lodging
- sub_domain=room_sales_reservations

{% enddocs %}