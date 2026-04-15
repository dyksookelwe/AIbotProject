import AIconfig
import os
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key= os.getenv('EXTRACTION_AI'), base_url=os.getenv('BASE_URL'))

class UserScheme(BaseModel):
    name: str | None = None
    goal: str | None = None
    format: str | None = None

def extract_data(text):
    extraction_prompt = """Ты специализированный экстрактор данных.Извлеки данные пользователя из сообщения. Правила:
    - Верни только имя, цель, формат.
    - Если данных нет — верни None
    - Не добавляй ничего лишнего
    Что извлекать:
    name - имя пользователя
    goal - цель обучения пользователя
    format - формат обучения пользователя (индивидуальный или групповой)
    Ответ:
    name: <имя или None>
    goal: <цель или None>
    format: <индивидуальный или групповой или None>"""
    message = [
    {
        "role": "system",
        "content": extraction_prompt
    },
    {
        "role": "user",
        "content": text
    }
    ]
    response = client.responses.parse(
        model=AIconfig.EXTRACTION_MODEL_NAME,
        input=message,
        temperature=AIconfig.TEMPERATURE,
        presence_penalty=AIconfig.PRESENCE_PENALTY,
        frequency_penalty=AIconfig.FREQUENCE_PENALTY,
        text_format=UserScheme
    )

    return response.output_parsed