from ai_logic import get_ai_answer

def rag_handler(text):
    answer = get_ai_answer(text)
    return answer