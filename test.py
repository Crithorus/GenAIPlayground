from langchain import OpenAI, HuggingFaceHub, PromptTemplate
from langchain.chains import SimpleSequentialChain

# Initialize the OpenAI LLM
openai_llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key='YOUR_OPENAI_API_KEY')

# Initialize the Hugging Face LLM (e.g., gpt2)
huggingface_llm = HuggingFaceHub(repo_id="gpt2", model_kwargs={"temperature": 0.7})

# Initialize the Gemini LLM (placeholder example, modify as needed for actual Gemini integration)
gemini_llm = OpenAI(model_name="gemini-model", openai_api_key='YOUR_GEMINI_API_KEY')  # Modify as needed

# Create a prompt template
prompt_template = PromptTemplate(input_variables=["text"], template="Translate this to French: {text}")

# Define a function to use a sequence with a switch for models
def run_sequence(text, model_name="openai"):
    # Select the appropriate LLM based on model_name
    if model_name == "openai":
        selected_llm = openai_llm
    elif model_name == "huggingface":
        selected_llm = huggingface_llm
    elif model_name == "gemini":
        selected_llm = gemini_llm
    else:
        raise ValueError(f"Unsupported model name: {model_name}")
    
    # Create the sequence chain
    def generate_prompt(text):
        return prompt_template.format(text=text)
    
    prompt_chain = SimpleSequentialChain(chains=[generate_prompt, selected_llm])
    
    # Execute the chain
    return prompt_chain.run({"text": text})

# Input text to translate
input_text = "Hello, how are you?"

# Execute the sequence using the desired model
selected_model = "openai"  # Change this to "huggingface" or "gemini"
response = run_sequence(input_text, model_name=selected_model)

# Output the result
print(f"Response from {selected_model}: {response}")
