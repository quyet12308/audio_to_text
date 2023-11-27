import datetime
import pytz
import json
def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t


def write_to_file(filename, error):
    content = {
        "time":gettime2(),
        "error":error
    }
    content_str = json.dumps(content)
    with open(filename, 'a') as file:
        file.write(content_str + '\n')

# write_to_file(
#     error="123",
#     filename="test1.txt"
# )