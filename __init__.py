from mycroft import MycroftSkill, intent_file_handler


class Interromperexercicio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('interromperexercicio.intent')
    def handle_interromperexercicio(self, message):
        self.speak_dialog('interromperexercicio')


def create_skill():
    return Interromperexercicio()

