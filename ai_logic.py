import os
import numpy as np
import AIconfig
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from data_processor import get_messages
load_dotenv()
VECTORS_FILE = AIconfig.VECTORS_FILE

client = OpenAI(api_key= os.getenv('AI_API_KEY'), base_url=os.getenv('BASE_URL'))
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

vectors_database = None
source_messages = []
messages = get_messages(AIconfig.FAQ_FILE)

def prepare_database(messages):
    global source_messages
    global vectors_database
    source_messages = messages
    if os.path.exists(VECTORS_FILE):
        print("There is saved vectors, downloading...")
        vectors_database = np.load(VECTORS_FILE)
        print(f"Download is success! There is {len(vectors_database)} vectors")
    else:
        print(f"There is no file with vectors, starting vectorization of {len(messages)} messages...")
        vectors_database = model.encode(messages)
        np.save(VECTORS_FILE, vectors_database)
    print("Success, vectors was created and saved to vectors_db.py")

def load_person():
    with open(AIconfig.PERSONA_FILE, 'r', encoding='utf-8') as f:
        system_prompt = f.read()
    return system_prompt

def get_ai_answer(user_text):
    query_vector = model.encode([user_text])
    similarities = cosine_similarity(query_vector, vectors_database)[0]
    top_indexes = np.argsort(similarities)[-15:]
    context_parts = []
    for i in top_indexes:
        context_parts.append(source_messages[int(i)])
    context_str = "\n\n".join(context_parts)

    system_prompt = load_person()
    message = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "system",
        "content": f"Используй этот контекст:\n{context_str}"
    },
    {
        "role": "user",
        "content": user_text
    }
]

    response = client.chat.completions.create(
        model=AIconfig.MODEL_NAME,
        messages=message,
        temperature=AIconfig.TEMPERATURE,
        presence_penalty=AIconfig.PRESENCE_PENALTY,
        frequency_penalty=AIconfig.FREQUENCE_PENALTY
    )
    print("CONTEXT:\n", context_str)


    return response.choices[0].message.content
