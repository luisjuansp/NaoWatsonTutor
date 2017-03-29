from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname


class Watson_Speech2Text:
    def __init__(self, username, password, learning=False, model=None):
        self.speech_to_text = SpeechToTextV1(
                username=username,
                password=password,
                x_watson_learning_opt_out=learning
        )
        self.model = model

    def recognize(self, audiofile, type):
        with open(join(dirname(__file__), audiofile),
                  'rb') as audio_file:
            result = self.speech_to_text.recognize(
                    audio_file, content_type=type, model=self.model)["results"][0]["alternatives"][0]["transcript"]

            print(result)
            return result

    def otrafuncion(self):
        return 0


# watson_speech2text = Watson_Speech2Text('5a43e79e-b9de-4b8b-9df2-bfaead00aaa6', '86WTJ13jYssQ')
#
# print(watson_speech2text.recognize("speech.wav", "audio/wav"))
