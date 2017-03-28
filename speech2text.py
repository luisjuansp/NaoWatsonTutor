import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
        username='5a43e79e-b9de-4b8b-9df2-bfaead00aaa6',
        password='86WTJ13jYssQ',
        x_watson_learning_opt_out=False
)

# print(json.dumps(speech_to_text.models(), indent=2))

speech_to_text.get_model('en-US_BroadbandModel')

# print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), './hello.wav'),
          'rb') as audio_file:
    result = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True,
            word_confidence=True)["results"][0]["alternatives"][0]["transcript"]

    print(result)
