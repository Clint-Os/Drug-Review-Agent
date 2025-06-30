
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain_core.documents import Document

import os
import pandas as pd

# Load your dataset
df = pd.read_csv('drug_reviews.csv')
df = df.dropna(subset=['DrugName', 'sideEffectsReview', 'condition', 'rating', 'effectiveness', 'sideEffects'])

# Use HuggingFace local embedding model (replace with yours if different)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Chroma DB setup
db_location = "./drug_reviews_db"
add_documents = not os.path.exists(db_location)

# Prepare documents if needed
documents = []
ids = []

if add_documents:
    for i, row in df.iterrows():
        document = Document(
            page_content=row['DrugName'] + ". " + row['sideEffectsReview'],
            metadata={
                'condition': row['condition'],
                'rating': row['rating'],
                'effectiveness': row['effectiveness'],
                'sideEffects': row['sideEffects']
            },
        )
        ids.append(str(i))
        documents.append(document)

# Create or load Chroma vector store
vector_store = Chroma(
    collection_name="drug_reviews",
    embedding_function=embeddings,
    persist_directory=db_location,
)

if add_documents:
    vector_store.add_documents(documents, ids=ids)

# Create retriever for use in chain
retriever = vector_store.as_retriever(search_kwargs={"k": 5})