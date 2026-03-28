import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_messages(filename):
    my_nick = os.getenv("TELEGRAM_NICK")
    raw_chats = os.getenv("TARGET_CHATS")
    if not raw_chats:
        return []
    target_chats = [chat.strip() for chat in raw_chats.split(',')]
    my_messages = []
    with open(f'{filename}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for chat in data['chats']['list']:
            if chat.get('name') in target_chats:
                for message in chat['messages']:
                    if message['type'] == 'message' and message.get('from') == my_nick:
                        if isinstance(message['text'], str) and len(message['text']) > 2 and "http" not in message['text']:
                            my_messages.append(message['text'].lower())
    return my_messages
