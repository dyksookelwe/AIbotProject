import AIconfig
import os
from openai import OpenAI

client = OpenAI(api_key= os.getenv('DEEPSEEK_API_KEY'), base_url=os.getenv('BASE_URL'))

def extract_name(text):
    extraction_prompt = """Извлеки имя пользователя из сообщения. Правила:
    - Верни только имя
    - Если имени нет — верни None
    - Не добавляй ничего лишнего
    Ответ:
    name: <имя или None>"""
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
    response = client.chat.completions.create(
        model=AIconfig.MODEL_NAME,
        messages=message,
        temperature=AIconfig.TEMPERATURE,
        presence_penalty=AIconfig.PRESENCE_PENALTY,
        frequency_penalty=AIconfig.FREQUENCE_PENALTY
    )

    return response.choices[0].message.content.srtip()

def extract_goal(text):
    extraction_prompt = """Извлеки цель прохождения курсов из сообщения. Правила:
    - Верни только цель
    - Если цели нет — верни None
    - Не добавляй ничего лишнего
    Ответ:
    goal: <цель или None>"""
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
    response = client.chat.completions.create(
        model=AIconfig.MODEL_NAME,
        messages=message,
        temperature=AIconfig.TEMPERATURE,
        presence_penalty=AIconfig.PRESENCE_PENALTY,
        frequency_penalty=AIconfig.FREQUENCE_PENALTY
    )
    return response.choices[0].message.content.srtip()

def extract_format(text):
    extraction_prompt = """Извлеки формат прохождения курсов из сообщения. Правила:
    - Верни только индивидуальный или групповой
    - Если формата нет — верни None
    - Не добавляй ничего лишнего
    Ответ:
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
    response = client.chat.completions.create(
        model=AIconfig.MODEL_NAME,
        messages=message,
        temperature=AIconfig.TEMPERATURE,
        presence_penalty=AIconfig.PRESENCE_PENALTY,
        frequency_penalty=AIconfig.FREQUENCE_PENALTY
    )
    return response.choices[0].message.content.srtip()