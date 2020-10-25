from rasa_nlu.model import Interpreter


class RasaNLU:
    def __init__(self):
        self.interpreter = Interpreter.load('./models/current/nlu')

    def get_values(self, text):
        return self.interpreter.parse(text)


if __name__ == '__main__':
    nlu = RasaNLU()
    values = nlu.get_values("Extract Image")

    print(values["intent"]["name"])
    for i in range(len(values['entities'])):
        print(values['entities'][i]["value"])
