from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI model with the API key
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    api_key=""
)

#create a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an intelligent chatbot. Answer the following question."),
        ("user", "{question}")
    ]
)

#initialize the output parser (to maintain the same format throughout the chatbot)
parser = StrOutputParser()

#create a chain using the prompt, LLM and the output parser
chain = prompt | llm | parser

#ask questions using the created chain

question = "what is generative AI"

response = chain.invoke({"question": question})
print(response)