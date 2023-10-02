import json
import boto3

dynamodb = boto3.client('dynamodb')
sqs = boto3.client('sqs')

def processPedido(event, context):
    if 'Records' in event:
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
    else:
        print("Evento não possui a chave 'Records'")

def enviarParaFilaSQS(event, context):
    if 'Records' in event:
        for record in event['Records']:
            evento = json.loads(record['body'])

            if evento['status'] == 'pronto':
                response = sqs.send_message(
                    QueueUrl='https://sqs.us-east-1.amazonaws.com/051246040808/espera-entrega',
                    MessageBody=json.dumps(evento)
                )

                print(f"Mensagem enviada para a fila de entrega: {response}")
    else:
        print("Evento não possui a chave 'Records'")
