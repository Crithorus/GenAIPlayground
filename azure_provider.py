# https://learn.microsoft.com/en-us/samples/azure-samples/function-python-ai-langchain/function-python-ai-langchain/
# https://github.com/azure-samples/function-python-ai-langchain/blob/main/function_app.py
# https://js.langchain.com/v0.2/docs/integrations/llms/azure/

from cloud_providers import CloudProviderInterface
from langchain_openai import AzureOpenAI
'''
OPENAI_API_TYPE=azure
AZURE_OPENAI_ENDPOINT=https://<azure openai resource name>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-05-01-preview
AZURE_OPENAI_API_KEY=<azure openai api key>
AZURE_OPENAI_GPT4O_MODEL_NAME=gpt-4o
AZURE_OPENAI_GPT4O_DEPLOYMENT_NAME=gpt-4o
'''
class AzureProvider(CloudProviderInterface):
    def invoke_llm(self,model_name,model_params,prompt):
        if model_name == "Azure":
            return self.call_openai_gpt(model_name,model_params,prompt)
        else:
            return "Model not supported"

    def call_openai_azure(prompt,model_params,model_name):
        try:
            # KIV for updates
            llm = AzureOpenAI(
                model_name = model_params.get("model_name"),
                temperature = model_params.get("temperature",0.7),
                max_retries= model_params.get("max_retries",2),
                max_tokens= model_params.get("max_tokens", 150),
                n = model_params.get("n",1),
                stop = model_params.get("stop",None)
            )
            return llm(prompt=prompt)
        except Exception as e:
            return f"Error occurred: {str(e)}"
