# Semantic Kernel: Natural Language (NL) to SQL Query Generation using Azure OpenAI (GPT-4 model)

In this repo we demonstrate how to use [Semantic Kernel](https://github.com/microsoft/semantic-kernel) to convert Natural Language (NL) to SQL Query using Azure OpenAI (GPT-4 model).

Semantic Kernel is an exciting framework and a powerful tool that can be used for several applications, including chatbots, virtual assistants, and more. 

This is a great way to make your data more accessible to non-technical users, and to make your applications more user-friendly.

Below are the main components of the Semantic Kernel:

![Orchestrating plugins with planner](./images/sk-kernel.png)

In the example of this repo, we developed the following plugin:

- **nlpToSqlPlugin**: This plugin is responsible for converting the Natural Language (NL) to SQL Query using Azure OpenAI (GPT-4 model).

As part of the plugin, we developed skills throught the use of [prompts](https://learn.microsoft.com/en-us/semantic-kernel/prompts/).

The following skill were developed:

- **ConvertNLPToSQL**: This skill is responsible for converting the Natural Language (NL) to SQL Query using Azure OpenAI (GPT-4 model).
- **MakeSQLCompatible**: This skill is responsible for making the SQL Query compatible with the Transact-SQL syntax.
- **WriteResponse**: This skill is responsible for writing the response to the user.

We also developed a [Native Function](https://learn.microsoft.com/en-us/semantic-kernel/agents/plugins/using-the-kernelfunction-decorator?tabs=python) to be able to interact with the database:

- **QueryDb**: This function is responsible for querying the database and returning the result.

With that, we can create a "Copilot like" experience, where the user can ask questions and the system will generate the SQL Query and return the result.

As our plugin has a lot of skills, we also developed a [Sequential Planner](https://learn.microsoft.com/en-us/semantic-kernel/agents/plugins/using-the-kernelfunction-decorator?tabs=python) to orchestrate the skills:

With the planner, we can orchestrate the skills in a sequence, so the system can generate the SQL Query and return the result.

The final result is a system that can convert Natural Language (NL) to SQL Query using Azure OpenAI (GPT-4 model).

## Requirements

- You must have a Pay-As-You-Go Azure account with administrator - or contributor-level access to your subscription. If you don't have an account, you can sign up for an account following the instructions.
- Get Access to [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)
- Once got approved create an Azure OpenAI in you Azure's subcription.
- Python 3.11
- You must have an Azure SQL Database with the tables and data you want to query. In this repo, we will use the a Sample database with some tables, which you can create using the scripts provided in the [folder](sql-scripts/create-tables.sql).
- You can use [generate-fake-data](generate-fake-data/generate-fake-data.py) script to populate the tables with some fake data.

## Install Required Libraries

```python
semantic-kernel==0.5.1.dev0
python-dotenv==1.0.0
openai==1.12.0
Faker==23.2.1
pyodbc==5.1.0
```

## Create .env file

```
CONNECTION_STRING=
AZURE_OPENAI_DEPLOYMENT_NAME=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
```

*You can rename the `.env.sample` to `.env` as well. Replace the values with your own data.*

## Quick Start

- Run `[generate-fake-data](generate-fake-data/generate-fake-data.py)` script to populate the tables with some fake data
- Run `main.py` to run the sample asks/questions detailed below.

## Sample - Questions/Asks

Below are some sample questions/asks that can be asked to the system and the responses that the system will generate.
These responses can be different based on the data in the database. If you use our generate-fake-data script, you may have different responses given the random nature of the data.

**Question/Ask 01**: I want to know how many transactions in the last 3 months

*Response*: According to the database query, the number of transactions is 26.

---

**Question/Ask 02**: Give me the name of the best seller in terms of sales volume in the whole period

*Response*: The seller's name according to the database query is John Doe.

---

**Question/Ask 03**: Which product has the highest sales volume in the last month

*Response*: According to the database query, the total sales volume for the product 'Nike Air Force 1' is 28.

---

## Adapt to your own data

Feel free to adapt the code to your own data. You can use your own data and modify the code to fit your needs.

- Replace the connection string in the `.env` file with your own connection string.
- Replace the Azure OpenAI API key and endpoint in the `.env` file with your own API key and endpoint.
- Replace the table's structure in [ConvertNLPToSQL](plugins/nlpToSqlPlugin/ConvertNLPToSQL/skprompt.txt) Plugin with your own table's structure.

## References

- <https://learn.microsoft.com/en-us/semantic-kernel/overview/>
- <https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/revolutionizing-sql-queries-with-azure-open-ai-and-semantic/ba-p/3913513>
- <https://github.com/microsoft/semantic-kernel>
- <https://medium.com/@ranjithkumar.panjabikesanind/orchestrate-ai-and-achieve-goals-combining-semantic-kernel-sequential-planner-openai-chatgpt-d23cf5c8f98d>
