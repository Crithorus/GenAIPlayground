from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import boto3
import google.generativeai as genai
import os
import helper_functions 

# Load env file
load_dotenv()
'''

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

# LLM Model Settings
llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature= 0.5)

# Prompmt Template 
ai_prompt = PromptTemplate.from_template('You are a super hero, Write a short speech about your {topic}')

# Chain
sequence = ai_prompt | llm

topic = "superpowers"
helper_functions.print_output(sequence.invoke({"topic": "saving the world"}))

'''

             
# Create an &BR; client in the &region-us-east-1; Region.
bedrock = boto3.client(
    service_name="bedrock",
    region_name = "us-east-1"
)
bedrock.list_foundation_models()