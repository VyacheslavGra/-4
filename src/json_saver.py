import json

from src.saver import Saver


class JSONSaver(Saver):
    """ Класс для записи в json-файл """

    def write_data(self, vacancies):
        """ Запись данных в json """

        data = self.get_data()
        data.extend(vacancies)

        self._write_data(data)

    def get_data(self):
        """ Получение данных json """

        try:
            with open(self._filename, encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def del_data(self):
        """ Удаление данных из файла """
        self._write_data([])

    def _write_data(self, data):
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)