import json
import boto3
from moto import mock_dynamodb2
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lambda_function import lambda_handler

# Verify that the response from your Lambda function has the expected format.

@mock_dynamodb2
def test_response_format():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='visitor_counter',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    table.put_item(Item={'id': 'counter', 'count': 0})

    response = lambda_handler({}, None)
    assert response['statusCode'] == 200

    body = json.loads(response['body'])
    assert 'visits' in body
    assert isinstance(body['visits'], int)
    assert body['visits'] >= 0

# Verify that the counter is actually incrementing between consecutive Lambda invocations.

@mock_dynamodb2
def test_incremental_behavior():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='visitor_counter',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    table.put_item(Item={'id': 'counter', 'count': 0})

    response1 = lambda_handler({}, None)
    visits1 = json.loads(response1['body'])['visits']

    response2 = lambda_handler({}, None)
    visits2 = json.loads(response2['body'])['visits']

    assert visits2 > visits1

# Garantir que o contador nunca diminui (não há decrementos).

@mock_dynamodb2
def test_no_decrement():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='visitor_counter',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    table.put_item(Item={'id': 'counter', 'count': 0})

    counts = []
    for _ in range(5):
        response = lambda_handler({}, None)
        visits = json.loads(response['body'])['visits']
        counts.append(visits)

    assert all(x <= y for x, y in zip(counts, counts[1:]))

# Testar como a Lambda reage a eventos inválidos ou None.

@mock_dynamodb2
def test_lambda_with_invalid_event():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    dynamodb.create_table(
        TableName='visitor_counter',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )

    response = lambda_handler(None, None)
    assert 'statusCode' in response
    assert response['statusCode'] in [200, 400, 500]
