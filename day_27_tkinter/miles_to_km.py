from tkinter import *
Font = "Ariel", 12, "bold"
window = Tk()
window.minsize(width=500, height=300)

miles_input = Entry()
miles_input["width"] = 10
miles_input.grid(column=1, row=0)
print(miles_input)

is_equ_to = Label(text="is equal to:", font=Font)
is_equ_to.grid(column=0, row=5)

km_label = Label(text="Km", font=Font)
km_label.grid(column=2, row=5)

miles_label = Label(text="Miles", font=Font)
miles_label.grid(column=2, row=0)

miles_answer = Label(font=Font)
miles_answer.grid(column=1, row=5)

def button_press():
    answer = miles_input.get()
    answer_int = int(answer) * 1.609344
    miles_answer["text"] = answer_int


    return answer

calculate_button = Button(text="calculate", command=button_press)
calculate_button["width"] = 7
calculate_button.grid(row=6, column=1)

window.mainloop()



