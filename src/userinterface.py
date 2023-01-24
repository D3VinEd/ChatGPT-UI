from tkinter import *
from src.api import api_request


def run_ui():
    root = Tk()
    app = ChatGPT(root)
    root.mainloop()


class ChatGPT:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat-GPT")
        self.master.geometry("1200x800")

        # Frames
        self.question_frame = Frame(self.master)
        self.question_frame.pack(pady=20)
        self.answer_frame = Frame(self.master)
        self.answer_frame.pack(pady=20)

        # Scrollbars
        self.question_scrollbar_x = Scrollbar(self.question_frame, orient='horizontal')
        self.question_scrollbar_x.pack(side=BOTTOM, fill=X)
        self.question_scrollbar_y = Scrollbar(self.question_frame, orient='vertical')
        self.question_scrollbar_y.pack(side=RIGHT, fill=Y)
        self.answer_scrollbar_x = Scrollbar(self.answer_frame, orient='horizontal')
        self.answer_scrollbar_x.pack(side=BOTTOM, fill=X)
        self.answer_scrollbar_y = Scrollbar(self.answer_frame, orient='vertical')
        self.answer_scrollbar_y.pack(side=RIGHT, fill=Y)

        # Question - Frame
        self.question = Text(self.question_frame, height=25, width=110, yscrollcommand=self.question_scrollbar_y.set,
                             xscrollcommand=self.question_scrollbar_x.set, wrap='none')
        # Button Absenden
        self.submit_button = Button(self.question_frame, text='Absenden', command=self.ask)
        self.submit_button.pack(side=BOTTOM, pady=5, padx=5)
        # Button Löschen
        self.clear_button = Button(self.question_frame, text="Löschen", command=lambda: self.question.delete(1.0, END))
        self.clear_button.pack(side=BOTTOM, pady=5, padx=5)

        # Scrollbar-Config
        self.question_scrollbar_y.config(command=self.question.yview)
        self.question_scrollbar_x.config(command=self.question.xview)

        self.question.pack(side=LEFT, fill=BOTH)

        # Answer - Frame
        self.answer = Text(self.answer_frame, height=25, width=110, yscrollcommand=self.answer_scrollbar_y.set,
                           xscrollcommand=self.answer_scrollbar_x.set, wrap='none')
        self.answer_scrollbar_y.config(command=self.answer.yview)
        self.answer_scrollbar_x.config(command=self.answer.xview)

        self.answer.pack(side=RIGHT)

    def ask(self):
        question = self.question.get(1.0, END)
        self.answer.delete(1.0, END)
        response = api_request(question)
        self.answer.insert(END, response)
