# import torch
# from transformers import Wav2Vec2ForCTC

# # Tải mô hình
# model = Wav2Vec2ForCTC.from_pretrained("models/pytorch_model.bin")

# # Xác định file âm thanh
# audio_file = "audio_test/510_cbsk___file_goc_510201920_3.wav"

# # Trích xuất đặc trưng âm thanh
# features = model.feature_extractor(audio_file, return_tensors="pt")

# # Thực hiện dự đoán
# logits = model(**features)

# # Giải mã dự đoán
# predicted_ids = torch.argmax(logits.logits, dim=-1)
# transcription = model.tokenizer.batch_decode(predicted_ids)

# # In kết quả
# print(transcription)



# import torch
# from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
# import torchaudio

# model_name = "nguyenvulebinh/wav2vec2-base-vietnamese-250h"  # Tên của mô hình bạn đã tải về
# model = Wav2Vec2ForCTC.from_pretrained(model_name)
# tokenizer = Wav2Vec2Tokenizer.from_pretrained(model_name)

# audio_file = "audio_test/510_cbsk___file_goc_510201920_7.wav"  # Đường dẫn đến file audio của bạn
# waveform, sample_rate = torchaudio.load(audio_file)

# input_values = tokenizer(waveform, return_tensors="pt").input_values

# with torch.no_grad():
#     logits = model(input_values).logits

# predicted_ids = torch.argmax(logits, dim=-1)
# transcription = tokenizer.batch_decode(predicted_ids)[0]

# print("Transcription:", transcription)
