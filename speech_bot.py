import os
from telegram.ext import (Updater, MessageHandler, Filters)

from text_to_audio import text_to_audio_file

# проверим наличие файла TOKEN в папке с ботом
filename = 'TOKEN.txt'
if os.path.exists(filename):
    with open(filename, 'r') as TOKEN_file:
        read_token = TOKEN_file.readline()
        print(f'{filename} прочитан')
else:
    print(f"Файл {filename} отсутствует в {os.getcwd()}")

# проверим наличие папки "audio_message" для храниея audio сообщений, и создадим ее если она отсутствует
if not os.path.isdir("audio_message"):
    os.mkdir("audio_message")
    print('папка "audio_message" создана')


def text_to_audio(update, context):
    file_name = text_to_audio_file(update.message.text)
    update.message.reply_voice(voice = open(file_name, 'rb'))


def del_mp3_file():
    for file_name in os.listdir('audio_message'):
        if file_name.endswith('.mp3'):
            del_file = os.remove(f'audio_message/{file_name}')


def main():
    TOKEN = read_token

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, text_to_audio)
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    del_mp3_file()
