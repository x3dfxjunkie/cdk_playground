{% for tag in table.all_tag_names -%}
CREATE TAG IF NOT EXISTS {{ environment }}_{{ tag_database }}.{{ tag_schema }}.{{ tag | upper | safe }};
{% endfor -%}
