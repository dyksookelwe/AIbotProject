from fsm_logic import fsm_handler
from rag_handler import rag_handler
user_states = {}
fsm_words = ["запис", "хочу купи", "купи"]
invalid_values = ["none", "не знаю", "неа", "нет", "хз", "None", ""]

def handle_user(user_id, text):
    text = text.lower()
    if user_id in user_states and user_states[user_id]["state"]:
        return fsm_handler(user_id, text)
    else:
        return route(user_id,text)

def route(user_id, text):
    if any(word in text for word in fsm_words):
        return fsm_handler(user_id, text)
    else:
        return rag_handler(user_id, text)
    
def is_valid(value):
    value = value.lower()
    if value in invalid_values:
        return False