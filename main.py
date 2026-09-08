from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# Ask user for prompt type
print("\n===== PROMPT GENERATOR =====")
print("1. Image Prompt")
print("2. Coding Prompt")
print("3. Writing Prompt")
print("4. Study Prompt")

choice = input("\nChoose a prompt type (1-4): ")

# Convert choice into a prompt type
if choice == "1":
    prompt_type = "image generation"
elif choice == "2":
    prompt_type = "coding"
elif choice == "3":
    prompt_type = "writing"
elif choice == "4":
    prompt_type = "study"
else:
    print("Invalid choice!")
    exit()

# Get user's idea
idea = input("Enter your idea: ")

# Prompt template
prompt = PromptTemplate(
    input_variables=["prompt_type", "idea"],
    template="""
You are a professional prompt engineer.

Create a high-quality prompt for {prompt_type}.

User's idea:
{idea}

Make the prompt detailed, clear, specific, and useful.

Return ONLY the final prompt.
"""
)

# Create LangChain chain
chain = prompt | llm

# Generate prompt
response = chain.invoke({
    "prompt_type": prompt_type,
    "idea": idea
})

# Display result
print("\n===== GENERATED PROMPT =====")
print(response.content[0]["text"])