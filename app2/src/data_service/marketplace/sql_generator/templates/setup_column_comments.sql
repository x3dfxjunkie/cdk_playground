{% for field in table.fields %}
{%- if field.comment %}
COMMENT ON COLUMN {{ environment }}_{{ table_database }}.{{ table_schema }}.{{ table.name | upper }}.{{ field.name }} 
IS '{{ field.comment }}';
{% endif %}
{% endfor %}