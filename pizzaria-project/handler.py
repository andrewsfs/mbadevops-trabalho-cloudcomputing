import json
import boto3

dynamodb = boto3.client('dynamodb')
sqs = boto3.client('sqs')

def processPedido(event, context):
    for record in event['Records']:
        evento = json.loads(record['body'])

        response = dynamodb.put_item(
            TableName='eventos-pizzaria',
            Item={
                'pedido': {'S': evento['pedido']},
                'status': {'S': evento['status']}
            }
        )

        print(f"Evento gravado no DynamoDB: {response}")

def enviarParaFilaSQS(event, context):
    for record in event['Records']:
        evento = json.loads(record['body'])

        if evento['status'] == 'pizza-pronta':
            response = sqs.send_message(
                QueueUrl='https://sqs.us-east-1.amazonaws.com/051246040808/espera-entrega',
                MessageBody=json.dumps(evento)
            )

            print(f"Mensagem enviada para a fila de entrega: {response}")
