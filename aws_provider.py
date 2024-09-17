import boto3
from langchain_aws import BedrockLLM
from cloud_providers import CloudProviderInterface
# Replace with your SageMaker endpoint name
endpoint_name = 'your-sagemaker-endpoint-name'

# Create a SageMaker runtime client
sagemaker_client = boto3.client('sagemaker-runtime')


class AWSProvider(CloudProviderInterface):
    def invoke_llm(self, model_name, model_params, prompt):
        try:
            # Initialize the Boto3 Bedrock client
            bedrock_client = boto3.client(
                'bedrock-runtime',
                region_name=model_params.get("region_name", "us-east-1"),
                aws_access_key_id=model_params.get("aws_access_key_id"),
                aws_secret_access_key=model_params.get("aws_secret_access_key"),
                aws_session_token=model_params.get("aws_session_token")  # If using temporary credentials
            )

            # Initialize the Bedrock LLM with the custom client
            llm = BedrockLLM(
                model_id=model_name,
                client=bedrock_client,  # Pass the custom Bedrock client
                model_kwargs={
                    "temperature": model_params.get("temperature", 0.7),
                    "max_tokens": model_params.get("max_tokens", 150),
                }
            )

            # Generate a response using the LLM
            response = llm(prompt)
            return response
        except Exception as e:
            return f"Error occurred: {str(e)}"
# https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api-ex-python.html
# https://python.langchain.com/docs/integrations/llms/bedrock/
# sample: https://python.langchain.com/docs/integrations/llms/bedrock/