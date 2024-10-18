from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory, ConversationSummaryMemory, ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


# load the GOOGLE_API_KEY
google_api_key =  os.getenv("GOOGLE_API_KEY")

llm =  ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0.2,          
)


# memory= ConversationBufferMemory()
memory= ConversationBufferWindowMemory(k=2) # it is mostly used
# memory= ConversationSummaryMemory(llm=llm) # to making the summery of llm
# memory= ConversationSummaryBufferMemory(llm=llm, max_token_limit=100) # to making the summery of llm with token limit


chain = ConversationChain(memory=memory,llm=llm)


while True:
    user_input = input("How I can help you!  ")
    if user_input == "exit":
        break
    response = chain.invoke(user_input)
    print("final==>>", response)