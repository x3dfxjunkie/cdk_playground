# Ingestion - Event Bridge Pipe - Validation Compute
This lambda function is used for validating all data coming through the ingestion event bridge pipe.  The event bridge pipe utilizes a lambda to process incoming data and perform the following:

1. start opentelemetry tracing
2. deserialize kinesis data
3. check if kinesis data is wrapped in a cloudevent envelope
    * unpack data from cloudevent
    * if telemetry data exists, extract telemetry data from cloudevent and set the opentelemetry parent context to the given traceid/parent span.
    * use incoming cloudevent attributes as base for new cloudevent attributes
3. for each event process incoming data
    * start telemetry and set telemetry context if exists
    * set span name to the event_id for easy identification in xray
    * add/override any cloudevent attributes that are necessary
    * package event into cloudevent
    * convert cloudevent to dictionary and append to success list
4. once all messages have been processed return the success list back to event bridge pipe to send to target