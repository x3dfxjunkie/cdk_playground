#!/bin/bash -e
echo "Running Fix for AWS Sec Manager Variables"
echo  $(echo $SF_CREDENTIALS | jq '.snowflake_rsa_key' | sed -e 's/^"//' -e 's/"$//') | base64 --decode > /home/helix/.ssh/snowflake.key
export PASSPHRASE=$(echo $SF_CREDENTIALS | jq '.snowflake_passphrase' | sed -e 's/^"//' -e 's/"$//')
#!/bin/bash
if [ -z "$SYNTHETIC_TYPE" -o -z "$SYNTHETIC_ID" ]; then
  echo "This script needs environment variables $SYNTHETIC_TYPE and $SYNTHETIC_ID to be set."
  exit 1
fi

# FORCE UPPERCASE
SYNTHETIC_TYPE=${SYNTHETIC_TYPE^^}
SYNTHETIC_ID=${SYNTHETIC_ID^^}

# make all non-alphanumeric characters into underscores
SYNTHETIC_ID=$(echo "$SYNTHETIC_ID" | tr -c '[:alnum:]' '_')
#remove trailing underscores if they exist
SYNTHETIC_ID=${SYNTHETIC_ID%_}
SYNTHETIC_ID=$(echo "$SYNTHETIC_ID" | tr '[:lower:]' '[:upper:]')

synthentic_type_raise="$SYNTHETIC_TYPE is not a proper SYNTHETIC_TYPE. Use any of the following -> USER, GROUP, FUNCTION."

if [[ "$SYNTHETIC_TYPE" =~ ^(USER|GROUP|FUNCTION)$ ]]; then
    :
else
    echo "$synthentic_type_raise"
fi

if [[ "$SYNTHETIC_TYPE" == "USER" ]]
then
     SYNTHETIC_TYPE_PREFIX="TSU"
     SYTHETIC_PASS=TRUE
elif [[ "$SYNTHETIC_TYPE" == "GROUP" ]]
then
     SYNTHETIC_TYPE_PREFIX="TSG"
     SYTHETIC_PASS=TRUE
elif [[ "$SYNTHETIC_TYPE" == "FUNCTION" ]]
then
    SYNTHETIC_TYPE_PREFIX="TSF"
    SYTHETIC_PASS=TRUE
else
    :
fi

if [[ $SYTHETIC_PASS ]]
then
    SYNTHETIC_SCHEMA="$SYNTHETIC_TYPE_PREFIX"_"$SYNTHETIC_ID"
    export SYNTHETIC_SCHEMA=$SYNTHETIC_SCHEMA
else
    echo "Did not set SYNTHETIC_SCHEMA. Use a accepted SYNTHETIC_TYPE."
fi
case $PROCESS in
    "run" ) 
        echo "--------RUN DBT RUN!!!-----------"
        cd /helix/dbt/mono/helix_mono
        dbt run $1;;
    * )
        echo "No Matching Command $PROCESS";;
esac
echo "Job Ending"