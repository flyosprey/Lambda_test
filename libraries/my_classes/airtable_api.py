import requests
from operator import itemgetter
from .constants import URL, HEADERS


class AirTableApi:

    def __init__(self):
        self.airtable_response = []
        self.airtable_records = []

    def get_data_from_api(self):
        response = requests.get(URL, headers=HEADERS)

        if not response.status_code == 200:
            return 'Not available page'

        self.airtable_response = response.json()
        self.airtable_records = (self.airtable_response["records"])

    def get_all_titles(self):
        self.get_data_from_api()

        for i in range(len(self.airtable_records)):
            self.airtable_records[i]["id"] = self.airtable_records[i]["fields"]["ID"]

        sorted_airtable_records = sorted(self.airtable_records, key=itemgetter('id'))

        titles = [sorted_airtable_records[i]["fields"]["title"] for i in range(len(sorted_airtable_records))]

        return titles
