from lub import *

class Controller:
    def __init__(self):
        super().__init__()

    def setView(self, view):
        self.view = view
        read_dict()

    def get_data(self):
        history = read_dict()
        return list(history.keys())

    def save_dialog(self):
        save_dialog()


    def get_forms(self, filter):
        history = read_dict()
        return history[filter]

    def edit_form(self, new_form, label):
        dict = read_dict()
        tmp = dict[str(self.view.word)]
        dict.pop(str(self.view.word))
        self.view.word = new_form.text
        dict[new_form.text] = tmp
        save_dict()
        label.text = 'Изменено'
        self.view.show_data_form(self.view.word)
        self.view.show_data('nan')

    def get_answer(self, answer):
        rez_plant, rez = analiz_question(answer.text)
        return find_in_base(rez_plant, rez)
