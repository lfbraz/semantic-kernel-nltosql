import semantic_kernel as sk
import asyncio
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.planning import SequentialPlanner
from dotenv import load_dotenv
import os
from plugins.QueryDb import queryDb as plugin
from semantic_kernel.planning import StepwisePlanner

# Get ROOT_DIR
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) )

# Take environment variables from .env.
load_dotenv(ROOT_DIR+'/.env', override=True)

async def create_plan(planner, input):
    return await planner.create_plan(goal=input)

async def invoke_plan(sequential_plan):
    return await sequential_plan.invoke()

async def main(nlp_input):
    
    kernel = sk.Kernel()
    
    # Get AOAI settings from .env
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()

    # Set the deployment name to the value of your chat model
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    azure_text_service = AzureChatCompletion(deployment_name=deployment, endpoint=endpoint, api_key=api_key)
    kernel.add_text_completion_service("azure_text_completion", azure_text_service)

    # Immport NLP to SQL Plugin
    plugins_directory = "plugins"
    kernel.import_semantic_plugin_from_directory(plugins_directory, "nlpToSqlPlugin")
    kernel.import_plugin(plugin.QueryDbPlugin(os.getenv("CONNECTION_STRING")), plugin_name="QueryDbPlugin")
    
    planner = SequentialPlanner(kernel)
    #planner = StepwisePlanner(kernel)

    # Create a plan with the NLP input
    ask = f"Create a SQL query according to the following request: {nlp_input} and query the database to get the result."

    plan = await create_plan(planner, ask)
 
    # Invoke the plan and get the result
    result = await invoke_plan(plan)

    print('/n')
    print(f'User ASK: {nlp_input}')
    print(f'Response: {result}')
    print('/n')
    
    # Print each step of the plan and its result
    for index, step in enumerate(plan._steps):
        print("Step:", index)
        print("Description:", step.description)
        print("Function:", step.plugin_name + "." + step._function.name)
        if len(step._outputs) > 0:
            print("  Output:\n", str.replace(result[step._outputs[0]], "\n", "\n  "))
            print("\n\n")


# Run the main function
if __name__ == "__main__":
    import asyncio

    asyncio.run(main("I want to know how many transactions in the last 3 months"))
    asyncio.run(main("Give me the name of the best seller in terms of sales volume in the whole period"))
    asyncio.run(main("Which product has the highest sales volume in the last month"))