from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for item in question_data:
    ques = Question(item["question"], item["correct_answer"])
    question_bank.append(ques)

quiz = QuizBrain(question_bank)

play = quiz.still_has_questions()
while play:
    quiz.next_question()
