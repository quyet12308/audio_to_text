from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os


def clear():
    os.system('clear')


checkpoint = "mr4/phobert-base-vi-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
def sentiment_analysis_1(text):
    # clear()
    # print("Ngày hôm nay của bạn thế nào?")
    # val = input("nhập text = ")
    raw_inputs = [text]
    inputs = tokenizer(raw_inputs, padding=True,
                    truncation=True, return_tensors="pt")
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

    # print(enumerate(predictions))
    print(predictions)
    print(type(predictions))
    data_list_result = predictions.tolist()[0]
    print(data_list_result)
    list_tag = ["negative","positive","neutral"]
    result_dict = dict(zip(list_tag, data_list_result))
    print(result_dict)
    return result_dict
    
    




    # gán với các key tiếng việt 
    # for i, prediction in enumerate(predictions):
    #     print(raw_inputs[i])
    #     sentiment_analysis_text_list = []
    #     for j, value in enumerate(prediction):
    #         sentiment_analysis_text = f"{model.config.id2label[j]} : {str(value.item())}"
    #         print(
    #             "    " + model.config.id2label[j] + ": " + str(value.item()))
    #         sentiment_analysis_text_list.append(sentiment_analysis_text)
    #     print(sentiment_analysis_text_list)
    #     print(type(sentiment_analysis_text_list))
    #     return sentiment_analysis_text_list


# clear()
# # print("Ngày hôm nay của bạn thế nào?")
# val = input("nhập text = ")
# raw_inputs = [val]
# inputs = tokenizer(raw_inputs, padding=True,
#                 truncation=True, return_tensors="pt")
# outputs = model(**inputs)
# predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
# clear()

# print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
# # print(enumerate(predictions))
# print(predictions)
# for i, prediction in enumerate(predictions):
#     print(raw_inputs[i])
#     sentiment_analysis_text_list = []
#     for j, value in enumerate(prediction):
#         sentiment_analysis_text = f"{model.config.id2label[j]} : {str(value.item())}"
#         print(
#             "    " + model.config.id2label[j] + ": " + str(value.item()))
#         sentiment_analysis_text_list.append(sentiment_analysis_text)
#     print(sentiment_analysis_text_list)
        
# print("<<<<<<<<<<<<<<<<<<<<<<<<<<")

# isStop = False
# while isStop == False:
#     text_input = input("nhap text = ")
#     output_text = sentiment_analysis_1(text=text_input)
#     print(output_text)
#     text_input2 = input("bạn muốn tiếp tục ko ? (y/n) = ")
#     if text_input2 == "n":
#         isStop = True
#     else:
#         continue

sentiment_analysis_1(text="hôm nay trời đẹp")