import aws_provider as aws_provider_bc 
import cloud_providers as cloud_providers_bc
import azure_provider as azure_provider_bc
import openai_provider as OpenAIProvider




        
def get_llm_invokers(self,provider_name):
        cloud_provider = self.get_cloud_provider(provider_name)
        return cloud_provider

class CloudProviderInterface:
    def invoke_llm(self,model_name,model_params,prompt):
        raise NotImplementedError("Subclasses must implement invoke_llm method")
    
class AWSProvider(CloudProviderInterface):
    def invoke_llm(self,model_name,model_params,promp):
        raise NotImplementedError("Subclasses must implement invoke_llm method")
    
class AzureProvider(CloudProviderInterface):
    def invoke_llm(self,model_name,model_params,promp):
        raise NotImplementedError("Subclasses must implement invoke_llm method")
    
# class OpenAIProvider(CloudProviderInterface):
#     def invoke_llm(self,model_name,model_params,promp):
#         raise NotImplementedError("Subclasses must implement invoke_llm method")    
    
class GoogleProvider(CloudProviderInterface):
    def invoke_llm(self,model_name,model_params,promp):
        raise NotImplementedError("Subclasses must implement invoke_llm method")
    

class CloudProviderFactory:
    def get_cloud_provider(self,provider_name):
        if provider_name == "AWS":
            return AWSProvider()
        elif provider_name == "Azure":
            return AzureProvider()
        elif provider_name == "OpenAI":
            return OpenAIProvider()
        else:
            raise ValueError(f"Unsupported cloud provider: {provider_name}")
        
cloud_provider_factory = CloudProviderFactory()
cloud_providers = cloud_provider_factory.get_cloud_provider("AWS")
llm_result = cloud_providers.invoke_llm(model_name="openai",model_params={"temperature":0.7},prompt="Write a story about a brave knight.")
