import os
from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.indexes import Index

# init
llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))

prompt_template = PromptTemplate("Please provide your question: {question}")
index = Index("knowledge_base.txt")

# Create the chain
chain = llm >> prompt_template >> index

# User input
question = "How can I return an item?"

# Perform the chain
response = chain(question)

# Print the response
print(response)
