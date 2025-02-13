# API Busca-Elástica

## Descrição
Este projeto consiste em uma API desenvolvida em Flask para processar arquivos CSV, inseri-los em um banco de dados e indexá-los no Apache Solr, no intuito de fazer buscas elásticas. A infraestrutura do projeto é gerenciada utilizando Docker Compose, permitindo a inicialização simultânea dos serviços necessários.

## Estrutura do Projeto
- **API Flask**: Responsável por baixar e processar arquivos CSV, inserindo os dados no banco de dados e realizando a indexação no Solr.
- **Apache Solr**: Ferramenta de busca utilizada para indexação e consulta eficiente dos dados processados.
- **Docker Compose**: Gerencia os containers necessários para execução da API e do Solr.

## Configuração e Execução
O projeto utiliza `docker-compose` para facilitar a sua execução. Para subir todos os containers necessários, utilize o seguinte comando:

```sh
docker compose up -d
```

Esse comando irá iniciar os seguintes containers:
- **API Flask** (definida no `api.Dockerfile`)
- **Apache Solr** (definido no `solr.Dockerfile`)

## Dependências
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Flask](https://flask.palletsprojects.com/)
- [Apache Solr](https://solr.apache.org/)

## Desenvolvedores

[Alysson Pereira](),
[Vivaldo Vítor]()
