from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    curr_text = question['text']
    curr_answ = question['answer']

    curr_question = Question(curr_text, curr_answ)
    question_bank.append(curr_question)

my_quiz = QuizBrain(question_bank)

for _ in range(3):
    my_quiz.next_question()
