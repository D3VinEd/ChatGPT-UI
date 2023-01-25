from pathlib import Path
import json


class ResponseHandler:
    FILE_PATH = "data/conversations.json"

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def save(self):
        file_data = self.load_data()
        data = {'question': self.question, 'answer': self.answer}
        file_data.append(data)
        self.save_data(file_data)

    def load(self):
        return self.load_data()

    def load_data(self):
        file_path = Path(self.FILE_PATH)
        if file_path.is_file():
            with open(self.FILE_PATH, "r") as file:
                return json.load(file)
        else:
            return []

    def save_data(self, data):
        with open(self.FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)
