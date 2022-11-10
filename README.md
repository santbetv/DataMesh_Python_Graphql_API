# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [Python ]
- [Visual Studio Code](https://github.com/Microsoft/vscode)

#Info Spanish
App Azure function python con visual studio code Graphql, conexión a posibles datos en DataBricks para Procesos en tecnología Disruptiva DATAMESH

# Crear archivo local.settings.json a nivel de host.json, este es privativo global de cada proyecto para poder adicionar keys, CORS y demas elementos 


    ```json
    {
        "IsEncrypted": false,
        "Values": {
            "AzureWebJobsStorage": "",
            "FUNCTIONS_WORKER_RUNTIME": "python",
            "AccessTokenDatabricks": "TOKENDEDATABRI"
        },
        "Host": {
            "CORS": "*"
        }
    }
    ```
## Comandos importantes para corer el proyecto en visual
- Tener configurado el entorno para ejecutar Azure Function Python
- func host start
- .venv\Scripts\python -m pip install -r requirements.txt
- .venv\Scripts\python -m pip install --upgrade pip
- pip freeze > requirements.txt
- 

## Referencias

[How To Create Azure Functions In Python, Create python Azure Function in Visual Studio Code](https://www.youtube.com/watch?v=FCmLLc9U6IY) <br />
[GraphQL: la alternativa flexible a REST para programar API](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/graphql/) <br />
[Build Azure Functions faster with VS Code](https://www.youtube.com/watch?v=9bMsdBYy-D0) <br />
[Learn GraphQL in python using Graphene in 45 Minutes](https://www.youtube.com/watch?v=_XIZnakIl3s) <br />
[GraphQL and FastAPI integration](https://www.youtube.com/watch?v=2_puWfTK8bQ) <br />
[Evaluación de Data Lakes en Machine Learning y Big Data](https://repositorio.unican.es/xmlui/bitstream/handle/10902/20973/Lopez%20Murcia%20Marina.pdf?sequence=1&isAllowed=y) <br />
[graphql.org/code/#python](https://graphql.org/code/#python) <br />
[Que es graphql](https://graphql.org/) <br />
[Implementación de GraphQL API como una función de Azure](https://docs.microsoft.com/es-es/azure/developer/javascript/how-to/with-web-app/graphql/azure-function-hello-world) <br />
[Create a Python function in Azure from the command line](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-powershell%2Ccmd%2Cbrowser) <br />
[Ejemplo azurefunctions-graphql](https://github.com/moyota/azurefunctions-graphql/tree/master/MyFunctionProj) <br />
[HttpResponse Class](https://docs.microsoft.com/en-us/python/api/azure-functions/azure.functions.httpresponse?view=azure-python) <br />
[Queries and Mutations](https://graphql.org/learn/queries/) <br />
[Databricks SQL Connector for Python](https://docs.databricks.com/dev-tools/python-sql-connector.html#description-attribute) <br />
[host.json reference for Azure Functions 2.x and later](https://docs.microsoft.com/en-us/azure/azure-functions/functions-host-json) <br />
[Developing GraphQL using Azure Function, Yanuar Singgih, Python Everywhere](https://www.youtube.com/watch?v=wOsRQ5ceeEU) <br />
[Azure & GraphQL: GraphQL endpoint in Azure Functions, .Net and why!](https://www.youtube.com/watch?v=ixJWN6Teqdg&t=9s) <br />
[Graphql, Curso Practico con Nodejs y Mongodb](https://www.youtube.com/watch?v=Wl8O6wW4FJU) <br />
