CREATE OR REPLACE STREAM {{ environment }}_{{ stream_database }}.{{ stream_schema }}.{{stream_prefix}}_{{ table.name | upper }}_STREAM COPY GRANTS
ON TABLE {{ landing_database }}.{{ landing_schema }}.{{ table.name | upper }}
SHOW_INITIAL_ROWS = TRUE;
