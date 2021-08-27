from my_classes.airtable_api import AirTableApi
from my_classes.buffer_output import BufferOutput


if __name__ == "__main__":
    air = AirTableApi()
    titles = air.get_all_titles()
    buf = BufferOutput(titles)
    buf.buffer_manage()
