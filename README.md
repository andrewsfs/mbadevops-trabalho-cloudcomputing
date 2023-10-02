# Trabalho Final da disciplina de Cloud Computing
Nessa arquitetura um barramento do eventBridge vai receber todos os eventos de uma pizzaria. Desde o pedido até a entrega. Onde cada um dos eventos deve ser guardados no banco de dados dynamo e apenas os eventos de pizza pronta que devem ser adicionados a fila SQS que posteriormente deve ser consumida por outro lambda.

- **EventBridge:** pizzaria
- **DynamoDB:** eventos-pizzaria
- **SQS:** espera-entrega
- **Serverless:** pizzaria-project
