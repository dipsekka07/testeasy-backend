import json
from examiner.event.event_handler import call_event


def lambda_handler(event, context):
    # TODO implement
    response = call_event(event)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
