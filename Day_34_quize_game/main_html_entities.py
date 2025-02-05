from question_model import Question
from data import questions
from quiz_brain import QuizBrain
import html
from ui import Quiz_Ui

question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    ### Html Entities ###
    # codes for symbols e.g: !, ., ?, /
    # import html
    # use html.unescape("")
    question_text = html.unescape(question_text)
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print(len(question_bank))
quiz_interface = Quiz_Ui(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

#print("You've completed the quiz")
#print(f"Your final score was: {quiz.score}/{quiz.question_number}")
