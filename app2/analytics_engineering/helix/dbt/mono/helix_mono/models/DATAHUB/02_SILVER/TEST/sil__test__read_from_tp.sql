select *
from
{{ source('brz_dreams_rooms_reservations', 'tp') }}
limit 100