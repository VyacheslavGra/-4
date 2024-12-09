import requests
from requests import Response

from src.get_vacancies import GetVacanciesAPI


class HeadHunterAPI(GetVacanciesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page) -> Response:
        self._params["text"] = keyword
        self._params["per_page"] = per_page
        response = requests.get(self._url, params=self._params)
        if response.status_code != 200:
            raise ValueError('Неверный ответ от сервера')
        return response

    def get_vacancies(self, keyword: str, per_page: int):
        return self.get_response(keyword, per_page).json()["items"]