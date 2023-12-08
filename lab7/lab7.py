import random

answers = ["Так", "Ні", "Можливо", "Сконцентруйся і спробуй ще раз", "Не знаю", "Питання не чітке, спробуй інше"]

def configure_magic_ball(new_answers):
    global answers
    answers.extend(new_answers)

def charivna_kulka(question):
    if not isinstance(question, str) or question.strip() == "":
        return "Питання не може бути пустим або не рядком."

    return random.choice(answers)

configure_magic_ball(["Можливо", "Безумовно так", "Навіть не запитуй", "Моя відповідь - ні"])

result = charivna_kulka("чи впаде сьогодні сніг?")
print(result)
