FROM python:3.10.12

# Sao chép các tệp yêu cầu vào hình ảnh và cài đặt các gói phụ thuộc
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN apt-get update && apt-get install -y cmake
RUN apt-get update && apt-get install -y ffmpeg
RUN apt-get update && apt-get install nano
RUN pip3 install -r requirements.txt

# Sao chép mã nguồn ứng dụng vào hình ảnh
# COPY . /app
WORKDIR /app
COPY . .


# Khởi chạy ứng dụng FastAPI
CMD ["python", "rabbit_mq_connect.py"]