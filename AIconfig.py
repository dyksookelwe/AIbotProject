MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0.8
PRESENCE_PENALTY = 0.1
MAX_TOKENS = 80
FREQUENCE_PENALTY = 0.1

PERSONA_FILE = "persona.txt"
FAQ_FILE = "FAQ.TXT"

FEW_SHOT = [
    {"role": "user", "content": "привет, в наличии?"},
    {"role": "assistant", "content": "Здравствуйте! Уточните пожалуйста интересующую вас позицию."},
    {"role": "user", "content": "здравствуйте, запись на 12 завтра есть?"},
    {"role": "assistant", "content": "Добрый день! Да, завтра есть свободное место на 12:00"},
    {"role": "user", "content": "здрасьте, какая стоимость доставки?"},
    {"role": "assistant", "content": "Добрый вечер! Стоимость доставки зависит от вашей страны и города. Базовая стоимость доставки - 3€ "}
]