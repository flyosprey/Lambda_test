import requests
from operator import itemgetter
import json



def lambda_handler(event, context):
    api_key = "keylMkRVCV25NxOBl"
    url = "https://api.airtable.com/v0/appW1Vv1p4IHxtiWQ/tblX1jGmYZoqyHrlE"
    headers = {"Authorization": "Bearer " + api_key}

    response = requests.get(url, headers=headers)
    airtable_response = response.json()
    airtable_records = (airtable_response["records"])

    for i in range(len(airtable_records)):
        airtable_records[i]["id"] = airtable_records[i]["fields"]["ID"]

    sorted_airtable_records = sorted(airtable_records, key=itemgetter('id'))

    titles = [sorted_airtable_records[i]["fields"]["title"] for i in range(len(sorted_airtable_records))]
    
    return json.dumps(titles, ensure_ascii=False)
