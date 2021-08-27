from my_classes.airtable_api import AirTableApi
from my_classes.buffer_output import BufferOutput


if __name__ == "__main__":
    air = AirTableApi()
    titles = air.get_all_titles()
    buffer = BufferOutput(titles)
    buffer.buffer_manage()
