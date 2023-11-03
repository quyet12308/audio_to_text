import os

def delete_file(name_file):
    try:
        os.remove(name_file)
        print(f"Đã xóa file: {name_file}")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {name_file}")
    except PermissionError:
        print(f"Không có quyền xóa file: {name_file}")

delete_file(name_file="audio_cover_16khz\\audio_0.wav")