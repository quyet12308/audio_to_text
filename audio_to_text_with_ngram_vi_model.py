# import os, zipfile
# from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
# from datasets import load_dataset
# import soundfile as sf
# import torch
# # import kenlm
# from pyctcdecode import Alphabet, BeamSearchDecoderCTC, LanguageModel
# # import IPython

# def get_decoder_ngram_model(tokenizer, ngram_lm_path):
#     vocab_dict = tokenizer.get_vocab()
#     sort_vocab = sorted((value, key) for (key, value) in vocab_dict.items())
#     vocab = [x[1] for x in sort_vocab][:-2]
#     vocab_list = vocab
#     # convert ctc blank character representation
#     vocab_list[tokenizer.pad_token_id] = ""
#     # replace special characters
#     vocab_list[tokenizer.unk_token_id] = ""
#     # vocab_list[tokenizer.bos_token_id] = ""
#     # vocab_list[tokenizer.eos_token_id] = ""
#     # convert space character representation
#     vocab_list[tokenizer.word_delimiter_token_id] = " "
#     # specify ctc blank char index, since conventially it is the last entry of the logit matrix
#     alphabet = Alphabet.build_alphabet(vocab_list, ctc_token_idx=tokenizer.pad_token_id)
#     lm_model = kenlm.Model(ngram_lm_path)
#     decoder = BeamSearchDecoderCTC(alphabet,
#                                    language_model=LanguageModel(lm_model))
#     return decoder

