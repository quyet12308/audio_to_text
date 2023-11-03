import requests
from pydub import AudioSegment
from pydub.playback import play
import io
import os
import numpy as np
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import load_dataset
import soundfile as sf
import math

from sentiment_analysis_python_hugging_face import sentiment_analysis_1

processor = Wav2Vec2Processor.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h")
model = Wav2Vec2ForCTC.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h")
    
def download_cover_to_16khz_and_segment(url):
    # Tải âm thanh từ URL
    response = requests.get(url, verify=False)
    audio_data = response.content

    # Chuyển đổi dữ liệu âm thanh thành đối tượng AudioSegment
    audio = AudioSegment.from_file(io.BytesIO(audio_data))

    # Lấy thông tin từ đối tượng AudioSegment
    duration = len(audio)  # Độ dài âm thanh (thời gian tổng cộng)
    sample_rate = audio.frame_rate  # Tốc độ mẫu (số mẫu trên giây)
    channels = audio.channels  # Số kênh âm thanh
    print(f"duration = {duration} , sample_rate = {sample_rate} , channels = {channels}")

    # Chuyển đổi tần số mẫu thành 16kHz
    audio = audio.set_frame_rate(16000)

    # Lấy độ dài tối đa của mỗi đoạn nhỏ (10 giây)
    max_segment_duration = 10000

    # Tính số lượng đoạn nhỏ cần cắt
    num_segments = math.ceil(duration / max_segment_duration)

    # Chia đoạn âm thanh thành các đoạn nhỏ hơn
    audio_segments = []
    for i in range(num_segments):
        start_time = i * max_segment_duration
        end_time = (i + 1) * max_segment_duration
        segment = audio[start_time:end_time]
        audio_segments.append(segment)

    #info 2
    for segment in audio_segments:
        duration2 = len(segment)  # Độ dài âm thanh (thời gian tổng cộng)
        sample_rate2 = segment.frame_rate  # Tốc độ mẫu (số mẫu trên giây)
        channels2 = segment.channels  # Số kênh âm thanh
        print(f"duration = {duration2} , sample_rate = {sample_rate2} , channels = {channels2}")

    # Chuyển đổi đối tượng AudioSegment thành mảng numpy
    audio_arrays = [np.array(segment.get_array_of_samples()) for segment in audio_segments]

    return audio_arrays

def play_audio_from_url(url,start_num_samples,end_num_samples):
    
    text1 = ""
    audio_arrays = download_cover_to_16khz_and_segment(url=url)
    for i in audio_arrays:
        input_values = processor(i, return_tensors="pt", padding="longest").input_values
        print(input_values)
        # Truy cập các thông số của tensor
        print("Shape:", input_values.shape)
        print("Data type:", input_values.dtype)
        print("Device:", input_values.device)
        print("Requires gradient:", input_values.requires_grad)

        input_values = input_values.to(torch.float32)

        # retrieve logits
        logits = model(input_values).logits

        # take argmax and decode
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)
        print(transcription)
        print(type(transcription))
        text1 = text1 + " ".join(transcription)
    print(text1)
    sentiment_analysis = sentiment_analysis_1(text=text1)
    return {"text1":text1,"sentiment_analysis":sentiment_analysis}

    # In ra một số mẫu âm thanh đầu tiên
    # print(audio_array[start_num_samples:end_num_samples])
    # for i in range(num_samples):
    #     print(audio_array[:i])
    
    # return audio_array[:num_samples]

    # In ra mảng dữ liệu âm thanh
    # print(audio_array)
    # input_values = processor(audio_array, return_tensors="pt", padding="longest").input_values
    # print(input_values)
    # # Truy cập các thông số của tensor
    # print("Shape:", input_values.shape)
    # print("Data type:", input_values.dtype)
    # print("Device:", input_values.device)
    # print("Requires gradient:", input_values.requires_grad)

    # input_values = input_values.to(torch.float32)

    # # retrieve logits
    # logits = model(input_values).logits

    # # take argmax and decode
    # predicted_ids = torch.argmax(logits, dim=-1)
    # transcription = processor.batch_decode(predicted_ids)
    # print(transcription)
    # print(type(transcription))

# URL của file âm thanh bạn muốn tải và phát
# audio_url = "https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/in-0902291318-394068251-20230927-100858-1695784138.33311.wav"
# audio_url = "https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/in-842888879888-0328147825-20230927-171932-1695809972.36489.wav" # 44s
# audio_url = "https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/in-84911118460-0352306136-20230927-093429-1695782069.33031.wav"
audio_url = "https://nextxcall.nextcrm.vn:8443/monitor/2023/09/27/in-0902291318-394068251-20230927-100858-1695784138.33311.wav" # 27s

# Gọi hàm để phát âm thanh từ URL
a = play_audio_from_url(audio_url,2000,2500)
print(a)
