
ALTER TABLE {{ environment }}_{{ table_database }}.{{ table_schema }}.{{ table.name | upper }} 
SET TAG {% for tag in table.tags %}
    {{ environment }}_{{ tag_database }}.{{ tag_schema }}.{{ tag.split("=")[0] | upper | safe }}={{ tag.split("=")[1] | safe }}{{ "," if not loop.last }}
{%- endfor %};
{% for field in table.fields %}
ALTER TABLE {{ environment }}_{{ table_database }}.{{ table_schema }}.{{ table.name | upper }}
    MODIFY COLUMN {{ field.name }}
    SET TAG {% for tag, val in field.tags.items() %}
        {{ environment }}_{{ tag_database }}.{{ tag_schema }}.{{ tag | upper }}='{{ val }}'{{ "," if not loop.last }}
    {%- endfor %};
{% endfor %}