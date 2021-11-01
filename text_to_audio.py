import pyttsx3
import subprocess
import datetime

engine = pyttsx3.init(driverName = 'sapi5')


def text_to_audio_file(text):
    file_name = f"audio_message/message_{datetime.datetime.now().isoformat()}"
    engine.save_to_file(text, f'{file_name}.mp3')
    engine.runAndWait()
    subprocess.run(
        ["ffmpeg", '-i', f'{file_name}.mp3', '-acodec', 'libopus',
         f'{file_name}.ogg', '-y']
    )
    return f'{file_name}.ogg'
