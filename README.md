# API para Extração de Dados de Notas Fiscais de Serviço

## Descrição

Esta API tem como objetivo extrair os dados de qualquer nota fiscal de serviço de qualquer município. O projeto é desenvolvido utilizando o framework Flask.

## Requisitos

- Docker
- Docker Compose

## Configuração do Projeto

1. Clone este repositório:
    ```sh
    git clone https://github.com/danielAlbuquerque/nfse-ocr-extractor-gpt.git
    cd nfse-ocr-extractor-gpt
    ```

2. Copie o arquivo `env-example` para `.env` e preencha a variável `OPENAI_API_KEY`:
    ```sh
    cp env-example .env
    # Edite o arquivo .env e adicione a sua chave de API do OpenAI
    ```

3. Crie um projeto e um token de API em [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).

4. Adicione saldo no projeto em [https://platform.openai.com/settings/organization/billing/overview](https://platform.openai.com/settings/organization/billing/overview).

5. Habilite o GPT-4o em `Project > Limits > Model Usage > Allow or Block Models`.

6. Instale as dependências:
    ```sh
    docker-compose up
    ```

## Uso

Após iniciar o Docker Compose, a API estará disponível em `http://localhost:5100`. Você pode fazer requisições para os endpoints disponíveis para extrair dados de notas fiscais de serviço.

### Exemplo de Requisição

Para extrair dados de uma nota fiscal de serviço, você pode usar o seguinte comando `curl` ou importar o comando no postman em file > import:

```sh
curl --location 'http://localhost:5100/extract-data' \
--form 'payload=@"/Users/danielalbuquerque/Desktop/Screenshot 2024-07-05 at 19.49.30.png"'
