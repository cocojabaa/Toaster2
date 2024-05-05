import json

class Settings():
    def __init__(self):
        self.__settings_dict = json.load(open("settings.json", "r", encoding="utf-8"))

    def save(self):
        json.dump(self.__settings_dict, open("settings.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    def get_screenshots_quality(self, raw_data:bool = False) -> str:
        if raw_data:
            return self.__settings_dict['screenshots_quality']
        if self.__settings_dict['screenshots_quality'] == "hight":
            return "Высокое"
        else:
            return "Низкое"


    def set_screenshots_quality(self):
        if self.__settings_dict["screenshots_quality"] == "hight":
            self.__settings_dict["screenshots_quality"] = "low"
        else:
            self.__settings_dict["screenshots_quality"] = "hight"
        self.save()
