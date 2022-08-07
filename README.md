# Delivery api
API que realiza o controle de pedidos de delivery.
*
## Desenvolvimento:
* A API foi desenvolvida utilizando a linguagem de programação python, fazendo uso do framework Django, PostgreSQL como o banco de dados e o Docker como ambiente de desenvolvimento.
*
## 🧾Instruções para o Uso:
## *Pré-requisitos para usar a aplicação:*
* Docker .
* Python.
## *Instruções*:
* Clonar o seguinte repositório git clone https://github.com/Luiz-gabrielsilva/delivery-api.git
* Entre na pasta do app da aplicação delivery cd delivery
* Executar o comando docker-compose up
* Após tais passos a aplicação rodará na porta :8000.

### Rotas:
***
* Endpoint : /orders/
* Methods : GET, POST
* Token : Não necessário
* Action: method GET Lista todos os usuários cadatrados junto de seus pedidos
* Action: method POST Realiza o cadastro do cliente (inluindo pedido, nome e outros)
***
* Endpoint : /users/me/
* Methods: GET, DELETE
* Token : Necessário
* Action: method GET Lista os dados do usuário autenticado
* Action: method DELETE Deleta o usuário logado
***
* Endpoint : /orders/id/
* Methods : GET, DELETE, POST, PUT
* Token : Necessário
* Action: method PUT``` Adiciona um cliente (incluindo pedido, nome e outros)
* Action: method DELETE``` Exclui o cliente da ID cadastrada e seus dados
* Action: method GET``` Lista todos o usuário da ID cadastrada
