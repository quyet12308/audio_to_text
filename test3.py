# def map_to_array(batch):
#     speech = batch["file"].read()
#     batch["speech"] = speech
#     # print(batch)
#     return batch

# def cover_audio_to_text(audio_segment):
#     # load dummy dataset and read soundfiles

#     # audio_segments = process_audio(url)
#     ds = {
#         "speech": audio_segment
#     }

#     # tokenize
#     input_values = processor(ds["speech"], return_tensors="pt", padding="longest", sampling_rate=16000).input_values  # Batch size 1
#     # input_values = np.double(input_values)
#     print(type(input_values))
#     # retrieve logits
#     logits = model(input_values).logits

#     # take argmax and decode
#     predicted_ids = torch.argmax(logits, dim=-1)
#     transcription = processor.batch_decode(predicted_ids)

#     # print(transcription)
#     result = str(transcription[0])
#     return result


# a = cover_audio_to_text(file_path="test_wav\\segment_1.wav")
# print(a)
# print(type(a))

# files = get_file_paths(folder_path="test_wav")
# text = ""
# for i in files:
    
#     t = cover_audio_to_text(file_path=i)
#     text = text + t + " "
# print(text)

# bản hoạt động với âm thanh trực tiếp ko có file local

# is_work = True
# while is_work:
#     input_url = input("nhập url = ")
#     data_audio_list = process_audio(url=input_url)
#     text = ""
#     for audio_data in data_audio_list:
#         print(audio_data)
#         print(type(audio_data))
#         t = cover_audio_to_text(audio_segment=audio_data)
#         text = text + t + " "
#     print(text)
#     input_text = input("ban muốn tiếp tục ko ? (y/n)")
#     if input_text == "n":
#         is_work = False
#     else:
#         continue


# ngram_lm_model = get_decoder_ngram_model(processor.tokenizer, "models/vi_lm_4grams.bin")

# is_work = True
# while is_work:
#     input_url = input("nhập url = ")
    
#     # text = ""
#     # for i in file_list:
#     #     t = cover_audio_to_text(i)
#     #     text = text + t + " "
#     # print(text)
#     text = cover_audio_to_text2(url=input_url)
#     print(text)
#     input_text = input("ban muốn tiếp tục ko ? (y/n)")
#     if input_text == "n":
#         is_work = False
#     else:
#         continue