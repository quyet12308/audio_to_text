import requests
import soundfile as sf
import librosa
import io

def process_audio_from_url(url):
    # Tải file audio từ URL
    response = requests.get(url,verify=False)
    audio_content = response.content
    
    # Đọc audio từ byte stream
    audio, sr = sf.read(io.BytesIO(audio_content))
    
    # Resample audio về 16kHz
    resampled_audio = librosa.resample(audio, 16000)
    
    # Tiếp tục xử lý hoặc chuyển đổi thành dạng đầu vào cho model máy học của bạn
    # ...
    
    return resampled_audio

a = process_audio_from_url(url="https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/out-0906268586-1001-20230927-143937-1695800377.34854.wav")

print(a)