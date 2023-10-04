TelegramMessage = dict[str, int | str | bool | dict]

example_message_1: TelegramMessage = {
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

example_message_2: TelegramMessage = {
    "1": 910197276,
    "2": {
        "2-1-": 55,
        "2-2": {
            "2-2-1": 882646417,
            "2-2-2": False,
            "2-2-3": "Александр",
            "2-2-4": "Леонов",
            "2-2-5": "Rentgengl",
            "2-2-6": "ru"
        },
        "2-3": {
            "2-3-1": 882646417,
            "2-3-2": "Александр",
            "2-3-3": "Леонов",
            "2-3-4": "Rentgengl",
            "2-3-5": "private"
        },
        "2-4": 1585628272,
        "2-5": "Привет"
    }
}
