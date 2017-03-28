from watson_speech2text import Watson_Speech2Text
from watson_conversation import Watson_Conversation
from naoproxy import NaoProxy


class Tutor():
    def __init__(self):
        IP = "192.168.0.104"
        # broker = ALBroker("myBroker", "0.0.0.0", 0, IP, 9559)

        global nao
        nao = NaoProxy(IP, "nao")

        self.nao = nao

        self.filename = "record.wav"

        self.conversation = Watson_Conversation('6432cebe-14b4-4f93-8e73-12ccdb5891c2',
                                                'ccaNRkHB1Uqt', '2016-09-20',
                                                '21d88c8e-c0e8-48cb-bffb-61524417ae38')

        self.speech2text = Watson_Speech2Text('5a43e79e-b9de-4b8b-9df2-bfaead00aaa6', '86WTJ13jYssQ')

        response = self.conversation.message("hello")

        self.nao.say(response)

    def startConversation(self):

        recording = False

        while True:
            if self.nao.getFrontHeadStatus():
                break

            if recording:
                recording = self.nao.getRightBumperStatus()
                if not recording:
                    self.nao.endRecordAudio(self.filename)
                    self.nao.say(self.conversation.message(self.speech2text.recognize(self.filename, "audio/wav")))
            else:
                recording = self.nao.getRightBumperStatus()
                if recording:
                    self.nao.startRecordAudio(self.filename)


tutor = Tutor()
tutor.startConversation()
