from typing import Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()


# load the GOOGLE_API_KEY
google_api_key =  os.getenv("GOOGLE_API_KEY")

# Initialize an instance of the ChatGoogleGenerativeAI with specific parameters
llm =  ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the model to use
    temperature=0.2,            # Set the randomness of the model's responses (0 = deterministic, 1 = very random)
)



prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are fruits assistent, you have to act like answer about fruits questions "),
        SystemMessage(content="Please do not anything else, just answer the question related to fruites"),
    ]
)

# prompt = prompt_template.format()

# print(prompt)

while True:
    user_input = input("How I can help you!  ")
    if user_input == "exit":
        break
    prompt_template.append(HumanMessage(content=user_input))
    prompt = prompt_template.format()
    print("prompt_hisory: ",prompt)
    
    response = llm.invoke(prompt)
    print("LLM response: ",response.content)
    prompt_template.append(AIMessage(content=response.content))
    
    