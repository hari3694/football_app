import requests
import pandas as pd


class ExternalApiManager:
    headers = {"X-Auth-Token": "c033ff9e31114f06921d843179871e94"}
    base_url = "https://api.football-data.org"

    def get_areas(self):
        """
        Function to get the areas of having competitions
        :return:
        """
        url = f"{self.base_url}/v4/areas/"

        response = requests.request("GET", url, headers=self.headers)
        area_response = response.json()['areas']
        # area_df = pd.DataFrame(area_response)
        return area_response

    def get_competitions(self):
        """
        Function to get the competitions
        :return:
        """
        url = f"{self.base_url}/v4/competitions"
        response = requests.request("GET", url, headers=self.headers)
        competition_list = response.json()['competitions']

        # competition_df = pd.json_normalize(competition_list)
        response = []
        for item in competition_list:
            print(item), "=========="
            response.append({'code': item['code'], 'name': item['name'], "country": item['area']['name']})
        return response

    def get_teams(self, competition_code):
        """
        Function to get the teams in a competition
        :param competition_code:
        :return:
        """
        url = f"{self.base_url}/v4/competitions/{competition_code}/teams"
        response = requests.request("GET", url, headers=self.headers)
        teams_list = response.json()["teams"]
        # teams_df = pd.json_normalize(teams_list)
        return teams_list