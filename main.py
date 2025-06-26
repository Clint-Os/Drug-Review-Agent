from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # Assuming you have the retriever set up as shown in vector.py

model = OllamaLLM(model="llama3.2")

template = """
You are a helpful assistant who can answer questions about drug reviews
reviews. You will be given a list of reviews and a question about them. Your task is to provide a concise and accurate answer based on the reviews provided.
Make sure to focus on the key points from the reviews that directly relate to the question asked.

Here are the relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

while True:
    question = input("Ask your question (q to quit): ")
    if question.lower() == 'q':
        break
    
    reviews = retriever.invoke(question) 
    result = chain.invoke({"reviews": reviews, "question": question})
    print("Answer:", result)
    print("--------------------------------------------------")
    print("You can ask another question or type 'q' to quit.")
    