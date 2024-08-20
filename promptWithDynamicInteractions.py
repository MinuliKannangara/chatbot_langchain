from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI model with the API key
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    api_key=""
)

# create a prompt template for dynamic interaction
prompt = ChatPromptTemplate.from_messages(
    [
        # have provided a system message as an instruction
        SystemMessage(content="You are an intelligent chatbot. Answer the following question."),
        MessagesPlaceholder(variable_name="question")  # to store multiple messages (here we store only the question
    ]
)

# initialize the output parser (to maintain the same format throughout the chatbot)
parser = StrOutputParser()

# create a chain using the prompt, LLM and the output parser
chain = prompt | llm | parser

# ask questions using the created chain

question = "what is generative AI"

response = chain.invoke({"question": question})
print(response)
