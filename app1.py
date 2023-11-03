from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC ,AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset
import soundfile as sf
import torch
import os
import io
import numpy as np

import datetime
import json
import pytz

from download_audio import cover_audio_file_to_16khz_3,get_file_name,download_audio,save_data_for_history_of_dowload_audio_in_table
from segment_audio import segment
from test2 import process_audio

from sentiment_analysis_python_hugging_face import sentiment_analysis_1

from audio_preprocessing import convert_audio_to_16khz,get_audio_from_url,split_audio_into_clips
# from audio_to_text_with_ngram_vi_model import get_decoder_ngram_model

# load model and tokenizer
processor = Wav2Vec2Processor.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h")
model = Wav2Vec2ForCTC.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h")

checkpoint = "mr4/phobert-base-vi-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model2 = AutoModelForSequenceClassification.from_pretrained(checkpoint)

# cái này là chuẩn
# define function to read in sound file
def map_to_array(batch):
    speech, _ = sf.read(batch["file"])
    batch["speech"] = speech
    print(batch)
    return batch

def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t

def cover_audio_to_text(file_path):
    # load dummy dataset and read soundfiles
    ds = map_to_array({
        # "file": 'audio_test/510_cbsk___file_goc_510201920_7.wav'
        "file": file_path
    })

    # tokenize
    input_values = processor(ds["speech"], return_tensors="pt", padding="longest", sampling_rate=16000).input_values  # Batch size 1
    print(input_values)
    # Truy cập các thông số của tensor
    print("Shape:", input_values.shape)
    print("Data type:", input_values.dtype)
    print("Device:", input_values.device)
    print("Requires gradient:", input_values.requires_grad)
    # retrieve logits
    logits = model(input_values).logits

    # take argmax and decode
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)

    # print(transcription)
    result = str(transcription[0])
    return result


    # define function to read in sound file from URL
def map_to_array2(batch):
  url = batch["url"]
  audio_data = get_audio_from_url(url)
  audio_format = convert_audio_to_16khz(audio_data)
  clips = split_audio_into_clips(audio_format, 10)
  batch["speech"] = clips
  return batch

def cover_audio_to_text2(url):
    # load dummy dataset and read soundfiles from URL
    ds = map_to_array2({
        "url": url
    })

    # tokenize
    input_values = processor(ds["speech"], return_tensors="pt", padding="longest").input_values  # Batch size 1

    # retrieve logits
    logits = model(input_values).logits

    # take argmax and decode
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)

    print(transcription)
    # result = str(transcription[0])
    # return result
    return transcription



def get_file_paths(folder_path):
    file_paths = []  # Danh sách chứa các đường dẫn file

    # Duyệt qua tất cả các tệp và thư mục trong folder_path
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Tạo đường dẫn tuyệt đối cho từng file
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)

    return file_paths


# bản hoạt động với file local
is_work = True
while is_work:
    input_url = input("nhập url = ")
    file_name = get_file_name()
    download_audio(url=input_url,output_file_path=file_name)
    cover_audio_file_to_16khz_3(input_file_path=f"download_audio/{file_name}.wav",output_file=file_name)
    segment(audio_file_input=f"audio_cover_16khz/{file_name}.wav",audio_file_output=file_name)
    save_data_for_history_of_dowload_audio_in_table(file_name=file_name,format_file="wav",time=gettime2(),url=input_url)
    file_list = get_file_paths(folder_path=f"segment_audio/{file_name}")
    text = ""
    for i in file_list:
        t = cover_audio_to_text(i)
        text = text + t + " "
    print(text)
    a = sentiment_analysis_1(text=text)
    input_text = input("ban muốn tiếp tục ko ? (y/n)")
    if input_text == "n":
        is_work = False
    else:
        continue



