# Google drive docs API

Сервис предоставляющий API для создания файлов в Google drive.

### В данном проекте использовались следующие инструменты:

- python v3.11
- django v5.0.3
- djangorestframework v3.14
- python-dotenv v1.0.1
- pydrive2 v1.19

### API:

```
POST "/files/"
Параметры JSON : 
        {
        "name": "test.txt",
        "data": "текстовое содержимое файла"
        }
        
При выполнении запроса в Google drive будет создан документ 
с названием = name и содержимым = data
```

Для использования Google drive необходимо в папку src положить файл client_secrets.json 
c полученными при авторизации Google аккаунта токенами.

При запуске приложения необходимо создать .env файл используюя в качестве образца .env.example