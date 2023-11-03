import librosa
# import numpy as np

# def process_audio_from_url(url):
#     # Lấy âm thanh từ URL
#     audio, sr = librosa.load(url, sr=None)
    
#     # Chuyển đổi âm thanh thành dạng 16kHz
#     audio_resampled = librosa.resample(audio, sr, 16000)
    
#     # Tính toán số lượng mảnh âm thanh có độ dài 10s
#     audio_length = len(audio_resampled)
#     segment_length = 10 * 16000  # 10s * 16kHz
#     num_segments = audio_length // segment_length
    
#     # Chia âm thanh thành mảng các mảnh có độ dài 10s
#     audio_segments = np.array_split(audio_resampled[:num_segments*segment_length], num_segments)
    
#     return audio_segments
from io import BytesIO
import io
import requests
import numpy as np
from scipy.io import wavfile

def process_audio(url):
    # Lấy dữ liệu âm thanh từ URL
    response = requests.get(url, verify=False)
    audio_data = response.content

    # Chuyển đổi dữ liệu âm thanh thành mảng numpy
    sample_rate, audio_array = wavfile.read(io.BytesIO(audio_data))
    
    # Chuyển đổi âm thanh thành 16kHz
    target_sample_rate = 16000
    if sample_rate != target_sample_rate:
        resampled_array = np.interp(
            np.linspace(0, len(audio_array), int(len(audio_array) * target_sample_rate / sample_rate)),
            np.arange(len(audio_array)),
            audio_array
        ).astype(np.int16)
    else:
        resampled_array = audio_array
    
    # Chia âm thanh thành các mảng có độ dài 10s
    #test
    audio_array = audio_array.astype(np.float64)
    # segment_length = target_sample_rate * 10
    # num_segments = len(audio_array) // segment_length
    # audio_segments = np.array_split(audio_array[:num_segments * segment_length], num_segments)


    # Độ dài mỗi đoạn âm thanh (đơn vị: giây)
    segment_length = 10

    # Tính số mẫu âm thanh trong mỗi đoạn
    segment_samples = int(segment_length * sample_rate)

    # Tính số lượng đoạn âm thanh
    num_segments = int(np.ceil(len(audio_array) / segment_samples))

    audio_segments = []
    # Chia tệp âm thanh thành các đoạn nhỏ
    for i in range(num_segments):
        start = i * segment_samples
        end = (i + 1) * segment_samples
        segment = audio_array[start:end]
        audio_segments.append(segment)
    # return segment

    # segment_length = target_sample_rate * 10
    # num_segments = len(resampled_array) // segment_length
    # audio_segments = np.array_split(resampled_array[:num_segments * segment_length], num_segments)
    
    return audio_segments



# def check_sample_rate(audio_data):
#     # Tạo đối tượng BytesIO và ghi dữ liệu âm thanh vào đó
#     audio_stream = BytesIO(audio_data)
    
#     # Tạo một mảng âm thanh từ đối tượng BytesIO
#     audio, _ = librosa.load(audio_stream, sr=None)
    
#     # Lấy tần số lấy mẫu của âm thanh
#     sample_rate = librosa.get_samplerate(audio)
    
#     return sample_rate

# url = "https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/out-0906268586-1001-20230927-143937-1695800377.34854.wav"
# a = process_audio(url=url)
# print(a)
# for i in a:
    # b = check_sample_rate(i)
    # print(f"check audio = {b}")

# import requests
from pydub import AudioSegment
# from io import BytesIO

def get_audio_from_url(audio_url):
    response = requests.get(audio_url,verify=False)
    audio_content = response.content

    audio = AudioSegment.from_file(BytesIO(audio_content))
    return audio

# audio_response = get_audio_from_url(audio_url="https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/out-0906268586-1001-20230927-143937-1695800377.34854.wav")

# print(audio_response)
