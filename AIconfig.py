import os

MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0.8
PRESENCE_PENALTY = 0.1
MAX_TOKENS = 80
FREQUENCE_PENALTY = 0.1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

FAQ_FILE = os.path.join(DATA_DIR, "FAQ.txt")
PERSONA_FILE = os.path.join(DATA_DIR, "persona.txt")
VECTORS_FILE = os.path.join(DATA_DIR, "vectors.db.npy")

FEW_SHOT = [
    {"role": "user", "content": "привет, в наличии?"},
    {"role": "assistant", "content": "Здравствуйте! Уточните пожалуйста интересующую вас позицию."},
    {"role": "user", "content": "здравствуйте, запись на 12 завтра есть?"},
    {"role": "assistant", "content": "Добрый день! Да, завтра есть свободное место на 12:00"},
    {"role": "user", "content": "здрасьте, какая стоимость доставки?"},
    {"role": "assistant", "content": "Добрый вечер! Стоимость доставки зависит от вашей страны и города. Базовая стоимость доставки - 3€ "}
]