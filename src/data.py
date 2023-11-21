TelegramMessage = dict[str, int | str | bool | dict]


example_message: TelegramMessage = {
    "update_id": 910197276,
    "message": {
        "message_id": 55,
        "from": {
            "id": 882646417,
            "is_bot": False,
            "first_name": "Александр",
            "last_name": "Леонов",
            "username": "Rentgengl",
            "language_code": "ru"
        },
        "chat": {
            "id": 882646417,
            "first_name": "Александр",
            "last_name": "Леонов",
            "username": "Rentgengl",
            "type": "private"
        },
        "date": 1585628272,
        "text": "Привет"
    }
}
