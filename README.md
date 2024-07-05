# API para Extração de Dados de Notas Fiscais de Serviço

## Descrição

Esta API tem como objetivo extrair os dados de qualquer nota fiscal de serviço de qualquer município. O projeto é desenvolvido utilizando o framework Flask.

## Requisitos

- Docker
- Docker Compose

## Configuração do Projeto

1. Clone este repositório:
    ```sh
    git clone [<URL_DO_REPOSITORIO>](https://github.com/danielAlbuquerque/nfse-ocr-extractor-gpt)
    cd nfse-ocr-extractor-gpt
    ```

2. Copie o arquivo `env-example` para `.env` e preencha a variável `OPENAI_API_KEY`:
    ```sh
    cp env-example .env
    # Edite o arquivo .env e adicione a sua chave de API do OpenAI
    ```

3. Instale as dependências:
    ```sh
    docker-compose up
    ```

## Uso

Após iniciar o Docker Compose, a API estará disponível em `http://localhost:5100`. Você pode fazer requisições para os endpoints disponíveis para extrair dados de notas fiscais de serviço.

## Licença

Este projeto está licenciado sob a Licença GPL.

## Versão

1.0
