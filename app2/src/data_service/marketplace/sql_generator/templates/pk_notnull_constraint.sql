

{% if table.unique_identifier is defined and table.unique_identifier | length -%}
ALTER TABLE {{ environment }}_{{ table_database }}.{{ table_schema }}.{{ table.name | upper }}
ALTER {% for uniq_id in table.unique_identifier %}{{ uniq_id | safe }} DROP NOT NULL{{ "," if not loop.last}}{% endfor %};{% endif -%}