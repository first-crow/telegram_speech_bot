import pyttsx3
import subprocess
import datetime


def text_to_audio_file(text):
    engine = pyttsx3.init(driverName='sapi5')
    base_file_name = 'message'
    suffix_name = datetime.datetime.now().strftime('%H-%M')
    mp3_file_name = ('_'.join([base_file_name, suffix_name]) + '.mp3')
    ogg_file_name = ('_'.join([base_file_name, suffix_name]) + '.ogg')
    engine.save_to_file(text, f'audio_message/{mp3_file_name}')
    engine.runAndWait()
    subprocess.run(
        ["ffmpeg", '-i', f'audio_message/{mp3_file_name}', '-acodec', 'libopus', f'audio_message/{ogg_file_name}',
         '-y'])
    return f'audio_message/{ogg_file_name}'
