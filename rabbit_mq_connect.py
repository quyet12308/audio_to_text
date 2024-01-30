import pika
import json
from security_info import rabbit_mq_infor,urls
# from test6 import play_audio_from_url
from test_ctc_wav2vec2 import play_audio_from_url
from test7 import get_data_and_process_via_url
from get_time import *

def send_message(message,quese_name):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=urls["url_rabbitmq2"],
            port=rabbit_mq_infor["port"],
            virtual_host=rabbit_mq_infor["virtual_host"],
            credentials=pika.PlainCredentials(
                username=rabbit_mq_infor["user_name"],
                password=rabbit_mq_infor["password"]
            )
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=quese_name,durable=False)
    
    channel.basic_publish(
        exchange='',
        routing_key=quese_name,
        # routing_key='nextfarm_ai_message',
        body=message
    )
    connection.close()
    return {"mesage":'Message sent successfully'}

def send_mes_log(url_audio, processing_time, quese_name, message):
    log_mes = {
        "time": gettime2(),
        "message": message,
        "url_audio": url_audio,
        # "processing_time":f"{time_difference(start_time=t1,end_time=t2,unit='ms')} ms"
        "processing_time": processing_time,
    }
    log_mes_json = json.dumps(log_mes, ensure_ascii=False)
    send_message(message=log_mes_json, quese_name=quese_name)

def send_error_log( quese_name, error):
    log_mes = {
        "time": gettime2(),
        "error": str(error)
    }
    log_mes_json = json.dumps(log_mes, ensure_ascii=False)
    send_message(message=log_mes_json, quese_name=quese_name)


def listen_rabbitmq(queue_name):
    # Kết nối tới RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=urls["url_rabbitmq2"],
            port=rabbit_mq_infor["port"],
            virtual_host=rabbit_mq_infor["virtual_host"],
            credentials=pika.PlainCredentials(
                username=rabbit_mq_infor["user_name"],
                password=rabbit_mq_infor["password"]
            )
            )
            )
    channel = connection.channel()

    # Định nghĩa và khai báo hàng đợi
    channel.queue_declare(queue=queue_name,durable=True)

    # Hàm callback được gọi khi nhận được tin nhắn
    def callback(ch, method, properties, body):
        t1 = gettime3()
        request_data = body.decode()
        print("Received message:", request_data)
        print(type(request_data))
        request_data = json.loads(request_data)
        new_dict_data = get_data_and_process_via_url(dict_data=request_data)
        t2 = gettime3()
        send_mes_log(
            message=request_data,
            processing_time=time_difference(start_time=t1,end_time=t2,unit="ms"),
            quese_name=rabbit_mq_infor["quese_log_requirements"],
            url_audio=new_dict_data["recording_file"]
        )
        data3 = play_audio_from_url(url=new_dict_data["recording_file"],start_num_samples=2000,end_num_samples=6000)
        data4 = {
            "tenant_code": new_dict_data["tenant_code"],
            "callid":new_dict_data["callid"],
            "text": data3["text2"],
            "sentiment_analysis": data3["sentiment_analysis"]
        }
        json_data4 = json.dumps(data4,ensure_ascii=False)
        print(json_data4)
        send_message(message=json_data4,quese_name=rabbit_mq_infor["quese_push_data"])
        t2 = gettime3()
        send_mes_log(
            message=json_data4,
            processing_time=time_difference(start_time=t1,end_time=t2,unit="ms"),
            quese_name=rabbit_mq_infor["quese_log_results"],
            url_audio=new_dict_data["recording_file"]
        )


    # Bắt đầu lắng nghe trên hàng đợi
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print("Listening for messages. To exit, press CTRL+C")

    # Bắt đầu tiêu thụ tin nhắn
    channel.start_consuming()

# Sử dụng hàm listen_rabbitmq để lắng nghe trên hàng đợi 'my_queue'
# listen_rabbitmq(rabbit_mq_infor['quese_get_data'])

# send_message(message="test",quese_name=rabbit_mq_infor["quese_push_data"])

flag = True
while flag:
    try:
        listen_rabbitmq(queue_name=rabbit_mq_infor['quese_get_data'])
    except Exception as e:
        # Xử lý ngoại lệ (lỗi)
        print(f"Lỗi xử lý : {str(e)}")
        send_error_log(
            error=e,
            quese_name=rabbit_mq_infor["quese_log_error"]
        )
        # Bỏ qua URL lỗi và tiếp tục vòng lặp
        continue
