import os
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
VECTORS_FILE = 'vectors.db.npy'

client = OpenAI(api_key='ollama', base_url="http://localhost:11434/v1")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

vectors_database = None
source_messages = []
def prepare_database(history):
    global source_messages
    global vectors_database
    source_messages = history
    if os.path.exists(VECTORS_FILE):
        print("There is saved vectors, downloading...")
        vectors_database = np.load(VECTORS_FILE)
        print(f"Download is success! There is {len(vectors_database)} vectors")
    else:
        print(f"There is no file with vectors, starting vectorization of {len(history)} messages...")
        vectors_database = model.encode(history)
        np.save(VECTORS_FILE, vectors_database)
    print("Success, vectors was created and saved to vectors_db.py")

def get_ai_answer(user_text):
    query_vector = model.encode([user_text])
    similarities = cosine_similarity(query_vector, vectors_database)[0]
    top_indexes = np.argsort(similarities)[-10:]
    context_parts = []
    for i in top_indexes:
        context_parts.append(source_messages[int(i)])
    context_str = "\n".join(context_parts)
    # English prompt for international compatability
    system_prompt = (
        "Ты — цифровой клон автора. Твоя база памяти содержит реальные переписки.\n"
        f"ВОТ ТВОИ РЕАЛЬНЫЕ СООБЩЕНИЯ ДЛЯ ПРИМЕРА:\n{context_str}\n\n"
        "ТВОИ ПРАВИЛА:\n"
        "1. Пиши ТОЛЬКО строчными буквами (без заглавных).\n"
        "2. Не используй знаки препинания (точки, запятые), если можешь без них.\n"
        "3. Отвечай кратко, но ПО СУТИ. Не ограничивайся одним словом.\n"
        "4. Используй сленг и манеру речи из примеров выше.\n"
        "5. Будь живым человеком, а не роботом. Если в примерах есть маты — используй их к месту."
    )

    response = client.chat.completions.create(
        model="llama3:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        temperature=0.7,
        top_p=0.9,
        presence_penalty=0.1,
        frequency_penalty=0.1
    )

    return response.choices[0].message.content
