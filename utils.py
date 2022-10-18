import json
import os


def get_sessions():
    """ Возвращает пути ко всем файлам из папки sessions """
    sessions_paths = []
    for session in os.listdir('sessions'):
        path = os.path.join('sessions', session)
        sessions_paths.append(path)
    return sessions_paths


def mark_bad_session(session_file):
    """ Помещаем файл сессии в папку bad sessions """
    os.replace(os.path.join(os.getcwd(), session_file),
               os.path.join(os.getcwd(), session_file.replace('sessions', 'bad_sessions')))
