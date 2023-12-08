import random
import unittest

# Function to configure magic ball
def configure_magic_ball(new_answers: list):
    global answers
    answers.extend(new_answers)

# Function to get random answers
def charivna_kulka(question: str) -> str:
    if not isinstance(question, str) or question == "":
        return "Питання не може бути пустим або не рядком."

    return random.choice(answers)

# Test class for CharivnaKulka
class TestCharivnaKulka(unittest.TestCase):
    def setUp(self):
        global answers
        answers = ["Так", "Ні", "Можливо", "Сконцентруйся і спробуй ще раз", "Не знаю", "Питання не чітке, спробуй інше"]

    def test_valid_answer(self):
        result = charivna_kulka("Чи сьогодні буде дощ?")
        self.assertIn(result, answers)

    def test_return_type(self):
        result = charivna_kulka("Тестове питання")
        self.assertIsInstance(result, str)

    def test_empty_question(self):
        result = charivna_kulka("")
        self.assertEqual(result, "Питання не може бути пустим або не рядком.")

    def test_non_string_question(self):
        result = charivna_kulka(123)
        self.assertEqual(result, "Питання не може бути пустим або не рядком.")

if __name__ == "__main__":
    unittest.main()
