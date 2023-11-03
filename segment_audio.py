import soundfile as sf
import numpy as np
import os

def segment(audio_file_input,audio_file_output):

    # Đọc tệp âm thanh
    audio, sample_rate = sf.read(audio_file_input)

    # Độ dài mỗi đoạn âm thanh (đơn vị: giây)
    segment_length = 10

    # Tính số mẫu âm thanh trong mỗi đoạn
    segment_samples = int(segment_length * sample_rate)

    # Tính số lượng đoạn âm thanh
    num_segments = int(np.ceil(len(audio) / segment_samples))

    # Chia tệp âm thanh thành các đoạn nhỏ
    for i in range(num_segments):
        start = i * segment_samples
        end = (i + 1) * segment_samples
        segment = audio[start:end]

        # Lưu đoạn âm thanh vào tệp mới
        if not os.path.exists(f"segment_audio/{audio_file_output}"):
            os.makedirs(f"segment_audio/{audio_file_output}")
        segment_filename = f"segment_audio/{audio_file_output}/segment_{i}.wav"
        sf.write(segment_filename, segment, sample_rate)