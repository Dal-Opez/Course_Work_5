import requests
from config import hh_api_conf
class HHApi():

    def __init__(self, page: int = 0) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "page": page,
            "employer_id": hh_api_conf.get("company_ids"),
            "only_with_salary": hh_api_conf.get("only_with_salary"),
            "per_page": hh_api_conf.get("vacancies_per_page"),
            "area": hh_api_conf.get("area")
        }

    def get_vacancies(self):
        response = requests.get(self.url, params=self.params)
        return response.json()["items"]

    def get_employers_data(self):
        employers_list = [
            {
                "id": employer_id,
                "name": requests.get(f"https://api.hh.ru/employers/{employer_id}").json().get("name"),
                "url": requests.get(f"https://api.hh.ru/employers/{employer_id}").json().get("alternate_url"),
            }
            for employer_id in self.params.get("employer_id")
        ]
        return employers_list