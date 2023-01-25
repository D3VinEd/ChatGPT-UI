from pathlib import Path
import json


class ResponseHandler:
    FILE_PATH = "data/conversations.json"

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.file = Path(ResponseHandler.FILE_PATH)

        self.check_file_exists()
        self.save()

    def save(self):
        with open(ResponseHandler.FILE_PATH, "r+") as file:
            file_data = json.load(file)
            data = {
                'question':  self.question,
                'answer': self.answer
            }
            file_data.append(json.dumps(data, indent=4))
            file.seek(0)
            json.dump(file_data, file, indent=4)

    def load(self):
        with open(ResponseHandler.FILE_PATH, "r") as file:
            return json.load(file)

    def check_file_exists(self):
        if not self.file.is_file():
            f = open(ResponseHandler.FILE_PATH, "w")
            f.write("[]")
            f.close()
