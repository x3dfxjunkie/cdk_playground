-- Macro to get warehouse size from the model yml

{% macro get_warehouse_prehook() %}
    {% if execute %}
        {% set model_metadata = model %}
        {% set nodes = model.meta.environment_wh %}
        {% for node in nodes %}
            {% if node.env.upper() == var("environment").upper() %}
                {{print(node.wh)}}
                {% set query %}
                    use warehouse {{ node.wh }}
                {% endset %}
                {% do run_query(query) %} 
            {%endif%}
        {% endfor %}
    {%endif%}
{% endmacro %}