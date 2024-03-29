from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    text = data["text"]
    answer = data["answer"]
    newQuestion = Question(text, answer)
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)

while (quiz.still_has_question()):
    quiz.next_question()

print(f"You completed the quiz")
print(f"Your final score was {quiz.get_score()}/{quiz.question_number}")