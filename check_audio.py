import soundfile as sf

def check_audio(audio_file):
    # Đường dẫn đến tệp âm thanh
    # audio_file = "segment_6.wav"

    # Đọc thông tin tệp âm thanh
    info = sf.info(audio_file)

    # In tốc độ lấy mẫu
    print("Sampling rate:", info.samplerate)

# check_audio(audio_file="audio_cover_16khz/audio_0.wav")