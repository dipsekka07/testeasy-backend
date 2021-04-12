import boto3
from dynamodb_json import json_util
#from boto3.dynamodb.conditions import Key


def makeConnection():
    pass


def get_exam_detail_by_id(event_data):
    res = boto3.resource('dynamodb', region_name='ap-southeast-1')
    table = res.Table('exams')
    data = event_data
    print(data)
    response3 = table.get_item(Key={'exam_id': '1'})
    # print(response3['Item'])
    return json_util.loads(response3['Item'])


def get_all_exams(event_data):
    client = boto3.client('dynamodb', region_name='ap-southeast-1')
    # res = boto3.resource('dynamodb', region_name='ap-southeast-1')
    # table = res.Table('exams')
    # response = client.list_tables()
    response1 = client.scan(TableName='exams', AttributesToGet=[
        'exam_id', 'exam_name'
    ])
    response2 = json_util.loads(response1['Items'])
    return response2


def create_new_exam(event_data):
    return {}
