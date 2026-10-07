from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model=MODEL, groq_api_key=userdata.get("GROQ_API_KEY"), temperature=0.2)
data="""RAG stands for Retrieval-Augmented Generation. It is an AI framework that connects a Large Language Model (LLM) to external, private, or real-time data sources. Instead of relying only on the AI's memorized training data, RAG allows it to "look up" specific information to provide more accurate, up-to-date"""
chain = ChatPromptTemplate.from_template("Summarize in exactly 10 sentences:\n{data}") | llm | StrOutputParser()
chain.invoke({"data": data})