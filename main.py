from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

import google.generativeai as genai
import os
import helper_functions 
# Load env file
load_dotenv()

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))


# Show available models
# for model in genai.list_models():
#     print(model.name)

llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature= 0.5)
response = llm.invoke('write a paragraph about warhammer 40k')

helper_functions.print_output(response.content)