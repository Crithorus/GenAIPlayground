import openai
from cloud_providers import CloudProviderInterface
from langchain_openai import OpenAI
# Replace with your OpenAI API key
openai.api_key = 'your-api-key-here'


class OpenAIProvider(CloudProviderInterface):
    def invoke_llm(self,model_name,model_params,prompt):
        if model_name == "openai":
            return self.call_openai_gpt(model_name,model_params,prompt)
        else:
            return "Model not supported"

    def call_openai_gpt(prompt,model_params,model_name):
        try:

            llm = OpenAI(
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

# # Example usage
# prompt = "Write a poem about the sea."
# result = call_openai_gpt(prompt)
# print(result)


