from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

import config


def create_file_in_google_drive(file_name: str, file_content: str):
    """Создание файла в Google drive"""
    try:
        gauth = GoogleAuth()

        # Загрузка сохраненного токена
        gauth.LoadCredentialsFile("mycreds.txt")

        if gauth.credentials is None:

            # добавление функции автоматического обновление токена
            gauth.GetFlow()
            gauth.flow.params.update({"access_type": "offline"})
            gauth.flow.params.update({"approval_prompt": "force"})

            # Аутентификация и авторизация
            gauth.LocalWebserverAuth()

        elif gauth.access_token_expired:
            gauth.Refresh()

        else:
            # Авторизация с текущим токеном
            gauth.Authorize()

        # Сохранение учетных данных для последующего использования
        gauth.SaveCredentialsFile("mycreds.txt")

        # Создание файла и запись данных в файл с последующей загрузкой
        drive = GoogleDrive(gauth)

        file_metadata = {"title": f"{file_name}", "parents": [{"id": config.FOLDER_ID}]}
        file = drive.CreateFile(file_metadata)
        file.SetContentString(file_content)
        file.Upload()

    except Exception as ex:
        return f"При загрузке файла в Googke drive произошла ошибка: {ex}"
