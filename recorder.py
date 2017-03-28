from naoqi import ALProxy
import time
from ftplib import FTP

robot_IP = '192.168.0.104'
robot_PORT = 9559  # ----------> Connect to robot <----------
tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
audio = ALProxy("ALAudioDevice", robot_IP, robot_PORT)
record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
aup = ALProxy("ALAudioPlayer", robot_IP, robot_PORT)

# ----------> recording <----------
print 'start recording...'
record_path = '/home/nao/record.wav'
record.startMicrophonesRecording(record_path, 'wav', 16000, (0, 0, 1, 0))
time.sleep(3)
record.stopMicrophonesRecording()
print 'record over'

# -------Guardar a la compu
filename = 'record.wav'
file = open(filename, 'wb')

ftp = FTP(robot_IP)
ftp.login("nao", "nao")
ftp.retrbinary('RETR %s' % filename, file.write)
