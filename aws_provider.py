import boto3
import json

# Replace with your SageMaker endpoint name
endpoint_name = 'your-sagemaker-endpoint-name'

# Create a SageMaker runtime client
sagemaker_client = boto3.client('sagemaker-runtime')

def invoke_sagemaker_llm(prompt):
    # Prepare the input payload (the prompt)
    payload = {
        "input": prompt,
        "parameters": {
            "temperature": 0.7,  # Adjust based on your needs
            "max_length": 100    # Set max response length
        }
    }

    try:
        # Invoke the SageMaker endpoint
        response = sagemaker_client.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='application/json',
            Body=json.dumps(payload)
        )
        
        # Parse the response
        response_body = response['Body'].read().decode('utf-8')
        result = json.loads(response_body)
        
        # Extract the model's output (assuming a field called "generated_text")
        generated_text = result.get('generated_text', 'No output received')
        return generated_text

    except Exception as e:
        return f"Error occurred: {str(e)}"

# Example usage
prompt = "Write a story about a brave knight."
result = invoke_sagemaker_llm(prompt)
print(result)
