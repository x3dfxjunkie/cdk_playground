
ALTER TASK IF EXISTS {{ environment }}_{{ task_database }}.{{ task_schema }}.{{managed_artifacts_prefix}}_{{ table.name | upper }}_TASK {{task_action}};
