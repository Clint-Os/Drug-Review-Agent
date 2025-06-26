from langchain_ollama import OllamaEmbeddings 
from langchain_chroma import Chroma
from langchain_core.documents import Document

import os
import pandas as pd 

df = pd.read_csv('drug_reviews.csv')
df = df.dropna(subset=['DrugName', 'sideEffectsReview', 'condition', 'rating', 'effectiveness', 'sideEffects'])
embeddings = OllamaEmbeddings(model="mxbai-embed-large") # Ensure the model name is correct and matches the Ollama model you have installed

db_location = "./drug_reviews_db"
add_documents = not os.path.exists(db_location)

documents = []
ids = []

if add_documents:

    for i, row in df.iterrows():
        document = Document(
            page_content=row['DrugName'] + " " + row['sideEffectsReview'],
            metadata={
                'condition': row['condition'],
                'rating': row['rating'],
                'effectiveness': row['effectiveness'],
                'sideEffects': row['sideEffects']},
            id=str(i)  # Ensure the ID is a string
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="drug_reviews",
    embedding_function=embeddings,
    persist_directory=db_location,
)

if add_documents:
    vector_store.add_documents(documents, ids=ids) 

#now connect our llm to the vector store 
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}  # looks up k reviews and passes them to the llm.
) 