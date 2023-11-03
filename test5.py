import librosa
import io
from pydub import AudioSegment
import requests
import soundfile as sf
import numpy as np


requests.packages.urllib3.disable_warnings()

def process_audio_from_url(audio_url):
    try:
        # Tải audio từ URL
        response = requests.get(audio_url,verify=False)
        if response.status_code == 200:
            audio_data = io.BytesIO(response.content)
            print(audio_data)
            # # Đọc tệp WAV ban đầu
            # audio = AudioSegment.from_wav(audio_data)

            # # Đọc thông tin tệp âm thanh
            # info = sf.info(audio)

            # # In tốc độ lấy mẫu
            # print("Sampling rate:", info.samplerate)

            # # Chuyển đổi tần số mẫu thành 16kHz
            # audio = audio.set_frame_rate(16000)

            # audio = AudioSegment.from_file(audio_data)
            
            # # Chuyển audio về định dạng 16kHz (nếu nó không phải là 16kHz)
            # # if audio.frame_rate != 16000:
            # #     audio = audio.set_frame_rate(16000)

            # # Đọc thông tin tệp âm thanh
            # info = sf.info(audio)

            # # In tốc độ lấy mẫu
            # print("Sampling rate:", info.samplerate)
            
            # # Chuyển audio thành mảng numpy
            # audio_data = librosa.to_mono(audio.get_array_of_samples())
            
            # return audio_data
        else:
            print("Lỗi: Không thể tải audio từ URL.")
            return None
    except Exception as e:
        print(f"Lỗi: {str(e)}")
        return None


a = process_audio_from_url(audio_url="https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/in-19006129-0397115281-20230927-150825-1695802105.35148.wav")

print(a)