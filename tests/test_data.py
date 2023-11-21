from src.data import TelegramMessage


message_1: TelegramMessage = {
    "1": 910197276,
    "2": {
        "2-1-": 55,
        "2-2": {
            "2-2-1": 'first',
            "2-2-2": False,
            "2-2-3": "second",
            "2-2-4": True,
            "2-2-5": "third",
            "2-2-6": "being deleted",
        },
        "2-3": {
            "2-3-1": 882646417,
            "2-3-2": False,
            "2-3-3": "second - second",
            "2-3-4": True,
            "2-3-5": "second - third",
            "2-3-6": "editable",
        },
        "2-4": "third - first",
        "2-5": 1585628272,
    }
}

message_2: TelegramMessage = {
    "1": 910197276,
    "2": {
        "2-1-": 55,
        "2-2": {
            "2-2-1": 'first',
            "2-2-2": False,
            "2-2-3": "second",
            "2-2-4": True,
            "2-2-5": "third",
            "2-2-7": "added",
        },
        "2-3": {
            "2-3-1": 88,
            "2-3-2": False,
            "2-3-3": "second - second",
            "2-3-4": True,
            "2-3-5": "second - third",
            "2-3-6": "modified",
        },
        "2-4": "third - first",
        "2-5": 1585628272,
    },
    "3": 0,
}

result_message: TelegramMessage = {
    "+ 3": 0,
    "2": {
        "2-2": {
            "+ 2-2-7": "added",
            "- 2-2-6": "being deleted"
        },
        "2-3": {
            "+ 2-3-1": 88,
            "+ 2-3-6": "modified",
            "- 2-3-1": 882646417,
            "- 2-3-6": "editable"
        }
    }
}
