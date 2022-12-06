from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    curr_text = question['question']
    curr_answ = question['correct_answer']

    curr_question = Question(curr_text, curr_answ)
    question_bank.append(curr_question)

my_quiz = QuizBrain(question_bank)

while my_quiz.still_has_questions():
    my_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {my_quiz.score}/{len(my_quiz.question_list)}")
