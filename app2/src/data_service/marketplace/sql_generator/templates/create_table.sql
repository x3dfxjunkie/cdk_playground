CREATE OR REPLACE TABLE {{ environment }}_{{ table_database }}.{{ table_schema }}.{{ table.name | upper }}
    COPY GRANTS
    COMMENT="{{ table.comment }}"
(
    {%- for field in table.fields %}
    {{ field.padded_name | lower }} {{ field.type | upper }}{{ "," if not loop.last}}
    {%- endfor %}
    {% if table.unique_identifier is defined and table.unique_identifier | length -%}
    ,CONSTRAINT pk PRIMARY KEY ({% for uniq_id in table.unique_identifier %}{{ uniq_id | safe }}{{ "," if not loop.last}}{% endfor %}) NOT ENFORCED
    {% endif -%}
);
