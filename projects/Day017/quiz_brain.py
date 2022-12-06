# TODO: Asking the quesitons
# TODO: Cheking if the answer was correct
# TODO: Checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        curr_text = curr_question.text
        curr_answ = curr_question.answer
        self.question_number += 1

        user_answ = input(
            f"Q.{self.question_number}: {curr_text} (True/False): ")

        self.check_answer(user_answ, curr_answ)

    def check_answer(self, user_answ, curr_answ):
        if user_answ.lower() == curr_answ.lower():
            print("That's the correct answer!")
            self.score += 1
        else:
            print("Wrong answer :c")
        print(f"The correct answer was {curr_answ}")
        print(f"Your score is: {self.score}/{self.question_number}\n")
