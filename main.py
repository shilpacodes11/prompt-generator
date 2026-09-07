from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

# Create the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Prompt template
prompt = PromptTemplate(
    input_variables=["idea"],
    template="""
You are a professional prompt engineer.

Convert the user's simple idea into a detailed and effective AI prompt.

User's idea:
{idea}

Generate only the improved prompt.
"""
)

# Create chain
chain = prompt | llm

# Take input from user
idea = input("Enter your idea: ")

# Generate prompt
response = chain.invoke({"idea": idea})

print("\nGenerated Prompt:")
print(response.content)