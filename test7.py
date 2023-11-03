a = {"tenant_code":"ganghan","callid":"1697684966.67643","recording_file":"https:\/\/nextxcall.nextcrm.vn:8443\/monitor\/2023\/10\/19\/out-0972657901-307-20231019-100927-1697684966.67643.wav"}
b = "https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/in-0902291318-394068251-20230927-100858-1695784138.33311.wav"
d = {"tenant_code":"getfit","callid":"1697946139.3851","recording_file":"https:\/\/nextxcall.nextcrm.vn:8443\/monitor\/\/\/\/"}


# print(type(a))
# recording_file = a["recording_file"]

# # Thay thế các ký tự không mong muốn trong URL
# recording_file = recording_file.replace("\\/", "/")

# # In URL đã được chuyển đổi
# print(recording_file)

def get_data_and_process_via_url(dict_data):
    tenant_code = dict_data["tenant_code"]
    callid = dict_data["callid"]
    recording_file = dict_data["recording_file"]

    # Thay thế các ký tự không mong muốn trong URL
    recording_file = recording_file.replace("\\/", "/")

    return {
        "tenant_code": tenant_code,
        "callid": callid,
        "recording_file": recording_file
    }

# c = get_data_and_process_via_url(dict_data=d)
# print(c)