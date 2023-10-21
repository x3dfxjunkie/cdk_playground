{%- if environment_name | upper != 'PROD' -%}
use warehouse {{warehouse_name}};
use role {{role_name}};
{%- endif %}
use database {{database_name}};

EXECUTE IMMEDIATE $$
DECLARE
    DB_NAME STRING;
    SCH_NAME STRING ;
    COMMENTS STRING;
    BU_UNIT STRING;
    BU_OWNER_EMAIL STRING;
    IA_UNIT STRING;
    IA_OWNER_EMAIL STRING;
    TYPE STRING ;
    ETL_USER_NAME STRING;
    ADD_ROLE_MASTER STRING;
    ENVIRONMENT STRING;
    SCHEMA_APPROVAL_IND STRING;
    BAPPID STRING;
    PROC_NAME STRING;

BEGIN
    DB_NAME :='{{database_name}}';
    SCH_NAME :='{{schema_name}}';
    COMMENTS  := '{{comments}}';
    BU_UNIT :='{{bu_unit}}';
    BU_OWNER_EMAIL :='{{bu_owner_email}}';
    IA_UNIT := '{{ia_unit}}';
    IA_OWNER_EMAIL := '{{ia_owner_email}}';
    TYPE := '{{access_type}}' ;
    ETL_USER_NAME :='{{etl_user_name}}';
    ADD_ROLE_MASTER := '{{add_role_master}}';
    ENVIRONMENT := '{{environment_name}}';
    SCHEMA_APPROVAL_IND := '{{schema_approval_ind}}';
    BAPPID := '{{bappid}}';
    PROC_NAME := '{{proc_name}}';

    EXECUTE IMMEDIATE 'DESCRIBE SCHEMA  {{schema_name}}';
    RETURN 'SCHEMA ' || SCH_NAME || ' ALREADY EXISTS.';

EXCEPTION
    WHEN OTHER THEN
        EXECUTE IMMEDIATE 'CALL UTILITY_DB.UTILITY_SCHEMA.SP_CREATE_SCHEMA(
                            ''' || DB_NAME || ''',
                            ''' || SCH_NAME || ''',
                            ''' || BU_UNIT || ''',
                            ''' || BU_OWNER_EMAIL || ''',
                            ''' || IA_UNIT || ''',
                            ''' || IA_OWNER_EMAIL || ''',
                            ''' || COMMENTS || ''',
                            ''' || TYPE || ''',
                            ''' || ETL_USER_NAME || ''',
                            ''' || ADD_ROLE_MASTER || ''',
                            ''' || ENVIRONMENT || ''',
                            ''' || SCHEMA_APPROVAL_IND || ''',
                            ''' || BAPPID || ''',
                            ''' || PROC_NAME || ''')';
        RETURN 'SCHEMA ' || SCH_NAME || ' CREATED SUCCESFULLY.';
END$$;
