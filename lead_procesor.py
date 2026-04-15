from states import user_states
from extraction import extract_data

exit_words = ["не хочу", "передумал", "отмена","стоп"]

responses = {
     "name": "Подскажите, пожалуйста, как я могу к вам обращаться?",
     "goal": "Приятно познакомиться! Расскажите, какие цели вас интересуют в изучении языка?",
     "format": "Понял вас! А какой формат занятий вам ближе: индивидуально с преподавателем или в небольшой группе с другими студентами?",
     "lead": "Супер, всё готово! Вся информация у меня есть. Скоро с вами свяжется наш специалист и ответит на оставшиеся вопросы по оплате и расписанию. До связи!"
}

def lead_processment(user_id, text):
    if user_id not in user_states:
            user_states[user_id] = {
                "stage": "new",
                "name": None,
                "goal": None,
                "format": None
            }

    if any(word in text for word in exit_words):
        return """Понял вас 👍 Если захотите вернуться — я всегда здесь.
        Могу пока рассказать про курсы или ответить на вопросы 🙂"""
    
    user = user_states[user_id]
    user_data = extract_data(text).model_dump()


    for key in user:
         if user_data.get(key) is not None:
              user[key] = user_data[key]

    print(f"Extracted data from {user_id} user is {user}")

    if any(user.get(key) is not None for key in user.values()):
         user["stage"] = "collecting"
    elif all(user.get(key) is not None for key in user.values()):
         user["stage"] = "closing"
    eli

    if not user["name"]:
         return responses["name"]
    elif not user["goal"]:
         return responses["goal"]
    elif not user["format"]:
         return responses["format"]
    else:
         return responses["lead"]
    