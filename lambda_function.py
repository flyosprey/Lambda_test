from airtable_api import AirTableApi
from buffer_output import BufferOutput


if __name__ == "__main__":
    air = AirTableApi()
    titles = air.get_all_titles()
    buf = BufferOutput(titles)
    buf.buffer_manage()
