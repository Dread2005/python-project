from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
font = ["Arial", 14, "italic"]


class Quiz_Ui:
    
    def __init__(self, quiz_brain: QuizBrain):

        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)



        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white")
        self.text = self.canvas.create_text(150, 125, text="Question", font=font, width=290)
        self.canvas.grid(row=1, column=0, columnspa=2, sticky="nsew", pady=10)

        photo_wrong = PhotoImage(file="images/false.png")
        photo_right = PhotoImage(file="images/true.png")


        self.wrong_button = Button(image=photo_wrong)
        self.wrong_button.config(borderwidth=0, highlightthickness=0,
                                 command=self.cross_button)
        self.wrong_button.grid(column=0, row=2)

        self.right_button = Button(image=photo_right)
        self.right_button.config(borderwidth=0, highlightthickness=0,
                                 command=self.tick_button)
        self.right_button.grid(column=1, row=2)

        self.score = Label(bg=THEME_COLOR, text="Score", fg="white")
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"score: {self.quiz.score}/10")
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="No More Questions")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")


    def tick_button(self):
        answer = self.quiz.check_answer("true")
        self.give_feedback(answer)
        return answer
        # if answer:
        #     self.canvas.config(bg="green")
        # else:
        #     self.canvas.config(bg="red")



    def cross_button(self):
        answer = self.quiz.check_answer("false")
        self.give_feedback(answer)
        return answer
        # if answer:
        #     self.canvas.config(bg="green")
        # else:
        #     self.canvas.config(bg="red")

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

