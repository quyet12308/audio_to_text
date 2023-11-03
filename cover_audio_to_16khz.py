import librosa
import soundfile as sf
import numpy as np
from pydub import AudioSegment
from scipy.io import wavfile
from check_audio import check_audio

def cover_audio_file_to_16khz(input_link,output_link):
    

    # Load the audio file
    audio, sr = librosa.load(input_link)

    # Resample the audio to 16 kHz
    resampled_audio = librosa.resample()

    # Save the resampled audio to a new WAV file
    librosa.output.write(output_link, resampled_audio, 16000)

def cover_audio_file_to_16khz_3(input_file_path,output_file):

    # Đọc tệp WAV ban đầu
    audio = AudioSegment.from_wav(input_file_path)

    # Chuyển đổi tần số mẫu thành 16kHz
    audio = audio.set_frame_rate(16000)

    # Lưu tệp WAV mới
    
    audio.export(f"audio_cover_16khz/{output_file}.wav", format="wav")

    print("Đã chuyển đổi tần số mẫu thành 16kHz.")


def cover_audio_file_to_16khz_2(input_wav_file,output_wav_file):


    # Mở tệp âm thanh đầu vào
    audio, sample_rate = sf.read(input_wav_file)

    # Chuyển đổi tốc độ lấy mẫu thành 16 kHz (nếu chưa ở dạng 16 kHz)
    if sample_rate != 16000:
        audio_resampled = sf.resample(audio, 16000)
    else:
        audio_resampled = audio

    # Lưu tệp âm thanh đã chuyển đổi thành 16 kHz
    sf.write(output_wav_file, audio_resampled, 16000)

def convert_audio_to_16khz_4(input_audio):
    # Chuyển đổi tần số mẫu thành 16kHz
    output_audio = input_audio.set_frame_rate(16000)
    return output_audio


# input_link = "audio_test/out-0906268586-1001-20230927-143937-1695800377.34854.wav"
# output_link = "audio_cover_16khz/audio_test_cover1.wav"

# check_audio(audio_file=input_link)

# # cover_audio_file_to_16khz_2(input_wav_file=input_link,output_wav_file=output_link)
# # cover_audio_file_to_16khz(output_link=output_link,input_link=input_link)
# cover_audio_file_to_16khz_3(input_file_path=input_link,output_file_path=output_link)

# check_audio(audio_file=output_link)