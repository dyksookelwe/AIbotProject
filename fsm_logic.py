from states import user_states
from extraction import extract_name, extract_goal, extract_format
from rag_handler import rag_handler
from states import is_valid

exit_words = ["не хочу", "передумал", "отмена","стоп"]
question_words = ["сколько", "как", "где", "что", "цена"]

def fsm_handler(user_id, text):
    user_states.setdefault(user_id, {"state": None})
    
    if any(word in text.lower() for word in question_words):
        return rag_handler(text)

    if any(word in text for word in exit_words):
        user_states[user_id]["state"] = None
        return """Понял вас 👍 Если захотите вернуться — я всегда здесь.
        Могу пока рассказать про курсы или ответить на вопросы 🙂"""
    
    elif user_states[user_id]["state"] is None:
        user_states[user_id]["state"] = "asking_name"
        return "Отлично 😊 Как я могу к вам обращаться?"
    
    elif user_states[user_id]["state"] == "asking_name":
        temp_name = extract_name(text)
        print(f"\nExtracted name: {temp_name}\n")
        if not is_valid(temp_name):
            return "Похоже, я не смог распознать имя 🤔 Напишите его, пожалуйста, одним словом"
        user_states[user_id]["name"] = temp_name
        user_states[user_id]["state"] = "asking_goal"
        return f"Отлично, {temp_name} 👍 Какая у вас цель в изучении языка?"
    
    elif user_states[user_id]["state"] == "asking_goal":
        temp_goal = extract_goal(text)
        print(f"\nExtracted goal: {temp_goal}")
        if not is_valid(temp_goal):
            return "Не совсем понял 🤔 Напишите, пожалуйста, вашу цель (например: работа, экзамен, переезд)"
        user_states[user_id]["goal"] = temp_goal
        user_states[user_id]["state"] = "asking_format"
        return "Как вам удобнее заниматься? Индивидуально или в группе?"
    
    elif user_states[user_id]["state"] == "asking_format":
        temp_format = extract_format(text)
        print(f"\nExtracted format: {temp_format}")
        if not is_valid(temp_format):
            return "Напишите, пожалуйста: индивидуально или групповые занятия 🙂"
        user_states[user_id]["format"] = temp_format
        user_states[user_id]["state"] = None        
        return """Супер, спасибо! 🙌 Я передал вашу заявку менеджеру — скоро с вами свяжутся.
        Пока что могу рассказать подробнее про курсы или подобрать программу 😊"""