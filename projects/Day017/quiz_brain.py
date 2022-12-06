# TODO: Asking the quesitons
# TODO: Cheking if the answer was correct
# TODO: Checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        curr_text = curr_question.text
        curr_answ = curr_question.answer
        self.question_number += 1

        answer = input(
            f"Q.{self.question_number}: {curr_text} (True/False): ").capitalize()

        if answer == curr_answ:
            print("Correct")
        else:
            print("Incorrect")
