import json
import boto3

dynamodb = boto3.client('dynamodb')
sqs = boto3.client('sqs')

def processPedido(event, context):
    for record in event['Records']:
        # Extrair dados do evento
        evento = json.loads(record['body'])

        # Gravar evento no DynamoDB
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
        # Extrair dados do evento
        evento = json.loads(record['body'])

        if evento['status'] == 'pizza-pronta':
            # Enviar evento para a fila de entrega
            response = sqs.send_message(
                QueueUrl='URL-da-fila-de-entrega',  # Substitua pela URL da fila de entrega
                MessageBody=json.dumps(evento)
            )

            print(f"Mensagem enviada para a fila de entrega: {response}")
