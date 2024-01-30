from datetime import datetime
import datetime
import pytz

def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t

def gettime3():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S.%f")
    return t

def time_difference(start_time, end_time, unit='ms'):
    # Chuyển đổi thời gian thành đối tượng datetime
    start_datetime = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
    end_datetime = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S.%f')
    
    # Tính toán chênh lệch thời gian
    time_diff = end_datetime - start_datetime
    
    # Chuyển đổi sang đơn vị thời gian yêu cầu
    if unit == 'ms':
        time_diff = time_diff.total_seconds() * 1000
    elif unit == 's':
        time_diff = time_diff.total_seconds()
    elif unit == 'm':
        time_diff = time_diff.total_seconds() / 60
    elif unit == 'h':
        time_diff = time_diff.total_seconds() / 3600
    
    # Làm tròn kết quả đến 3 chữ số sau dấu thập phân
    time_diff = round(time_diff, 3)
    return time_diff

# Ví dụ sử dụng hàm
# start_time = '2024-01-18 12:30:00.000'
# end_time = '2024-01-18 12:30:01.500'

# # Tính chênh lệch thời gian trong đơn vị ms
# time_diff_ms = time_difference(start_time, end_time, 'ms')
# print(f'Time difference: {time_diff_ms} ms')

# t1 = gettime3()
# print("abc")
# t2 = gettime3()
# a = time_difference(start_time=t1,end_time=t2,unit="ms")
# print(a)