from tkinter import *
from src.api import api_request
from src.change_config import ConfigChanger
from src.texttospeech import text_to_speech
from configparser import ConfigParser


def run_ui():
    root = Tk()
    ChatGPT(root)
    root.mainloop()


class ChatGPT:
    """Creating a TKinter Userinterface with textboxes to ask ChatGPT and get the response"""
    def __init__(self, master):
        self.master = master
        self.master.title("Chat-GPT")
        self.master.geometry("950x600")
        self.master.resizable(0, 0)

        # Frames
        self.question_frame = Frame(self.master)
        self.question_frame.pack(pady=20, padx=10, fill=X)
        self.button_frame = Frame(self.master)
        self.button_frame.pack(pady=10, padx=10, fill=X)
        self.answer_frame = Frame(self.master)
        self.answer_frame.pack(pady=20, padx=10, fill=X)

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
        self.question = Text(self.question_frame, height=15, width=110, yscrollcommand=self.question_scrollbar_y.set,
                             xscrollcommand=self.question_scrollbar_x.set, wrap='none')
        self.question.pack(side=LEFT, fill=BOTH)

        # Button Absenden
        self.submit_button = Button(self.button_frame, text='Absenden', command=self.ask)
        self.submit_button.pack(side=LEFT, pady=5, padx=5)

        # Button Löschen
        self.clear_button = Button(self.button_frame, text="Löschen", command=lambda: self.question.delete(1.0, END))
        self.clear_button.pack(side=LEFT, pady=5, padx=5)

        # Button Settings
        self.settings_button = Button(self.button_frame, text="Einstellung", command=lambda: ConfigChanger(self.master))
        self.settings_button.pack(side=LEFT, pady=5, padx=5)

        # Answer - Frame
        self.answer = Text(self.answer_frame, height=15, width=110, yscrollcommand=self.answer_scrollbar_y.set,
                           xscrollcommand=self.answer_scrollbar_x.set, wrap='none')

        self.answer.pack(side=LEFT)

        # Scrollbar-Config
        self.question_scrollbar_y.config(command=self.question.yview)
        self.question_scrollbar_x.config(command=self.question.xview)
        self.answer_scrollbar_y.config(command=self.answer.yview)
        self.answer_scrollbar_x.config(command=self.answer.xview)

    def ask(self):
        config = ConfigParser()
        config.read('config/config.ini')
        self.answer.delete(1.0, END)
        question = self.question.get(1.0, END)
        response = api_request(question)
        self.answer.insert(1.0, response)
        print(config['SPEECH']['active'])
        if config['SPEECH']['active'] == str(1):
            text_to_speech(response)
