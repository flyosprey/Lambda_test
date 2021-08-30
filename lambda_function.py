from airtable_api import AirTableApi
from buffer_output import BufferOutput
import json


def lambda_handler(event, context):
    air = AirTableApi()
    titles = air.get_all_titles()
    buf = BufferOutput(titles)
    response = buf.buffer_manage()
    return json.dumps(response, ensure_ascii=False)
