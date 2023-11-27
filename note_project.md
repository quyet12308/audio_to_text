# Note dự án theo log ( quá trình làm - các lỗi gặp phải - hướng khắc phục)
- mục đích file này là để sau có dùng lại thì có thể hiểu và tiếp cận nhanh hơn

## 15/11/2023
- Vấn đề: Text sau khi chuyển đổi từ audio còn không được rõ ràng và lộn xộn ( độ chính xác khoảng 60 70 %)
- Nguyên nhân : Do chưa sử dụng đượng model n gram để làm mượt text đầu ra (mô hình n gram cho tiếng việt)
- Hướng khắc phục : Đã test qua loại kỹ thuật whishper của openAI (mục đích để trách pahir sử dụng model ngram đi kèm)
- Kết quả sau khi khắc phục : Không khả thi , do bị ăn bớt mất rất nhiều text của audio 
- 