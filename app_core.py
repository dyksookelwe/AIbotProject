from lead_procesor import lead_processment
from rag_handler import rag_handler
from states import user_states
lead_words = ["запис", "хочу купи", "купи"]

def handle_user(user_id, text):
    text = text.lower()
    return route(user_id,text)

def route(user_id, text):
    if any(word in text for word in lead_words):
        return lead_processment(user_id, text)
    else:
        return rag_handler(text)