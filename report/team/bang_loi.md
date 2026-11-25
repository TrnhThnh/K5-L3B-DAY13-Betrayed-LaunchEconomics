# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Hai thành viên xem mục “Hai mươi ca lỗi” trong đề Word và ghi 20 nhãn vào hai bản riêng trong 8 phút. Chốt cả hai bản rồi mới xem nhãn tham khảo, bảng khắc phục và đối chiếu. Giữ nguyên nhãn ban đầu khi điền cột “Nhãn thống nhất”.

Người gắn nhãn 1: Thinh · Người gắn nhãn 2: Đức

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** Chờ hai bộ nhãn. Đếm số ca trùng ở hai cột nhãn ban đầu rồi chia cho 20. Ngưỡng của bài là 16/20 (80%).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Chờ đối chiếu hai bộ nhãn để ghi quy tắc cho từng ca lệch.

<details>
<summary>Nhãn tham khảo cho 20 ca (mở sau khi chốt hai bộ nhãn)</summary>

| Loại lỗi | Ca |
| --- | --- |
| Do người dùng | 1, 6, 9, 14 |
| Hệ thống | 2, 7, 8, 15, 20 |
| Ngữ cảnh | 3, 10, 16, 18 |
| Giới hạn hệ thống | 4, 11, 13, 19 |
| Ngầm | 5, 12, 17 |

Đối chiếu với [hướng dẫn Lab 13, Nhiệm vụ C](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhiệm-vụ-c--bảng-lỗi-và-cách-khắc-phục-30-phút). Tỷ lệ đồng thuận được tính từ hai bộ nhãn của thành viên.

</details>

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Bảng dưới đây là phương án khắc phục đề xuất theo tình huống trong đề. Event và ngưỡng là đặc tả để triển khai và kiểm chứng trong pilot.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi `refund_account_validation_failed` kèm `trace_id`, mã ngân hàng và lý do sai độ dài. Cảnh báo khi tỷ lệ lỗi này vượt 2% số lượt nhập tài khoản trong ngày. | Kiểm tra định dạng theo ngân hàng trước khi gọi tool hoàn tiền. Giữ yêu cầu ở trạng thái chờ và cho khách sửa thông tin. | Trưởng nhóm trải nghiệm khách hàng |
| 15 | Hệ thống | Trước khi gửi, đối chiếu số hoàn đề xuất với số hoàn tính từ thời gian giao trễ và phiên bản chính sách. Ghi `refund_policy_mismatch` với `trace_id` cho mọi trường hợp lệch trên 0 đ. | Chặn gửi khi số tiền lệch, chuyển người duyệt cùng cách tính theo chính sách và thêm ca biên 24–48 giờ vào bộ kiểm thử. | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Ghi `refund_notification_sent` kèm `trace_id`, múi giờ và giờ gửi địa phương. Kiểm tra mỗi ngày, cảnh báo nếu có bất kỳ thông báo thường nào gửi trong khoảng 22:00–07:00. | Xếp hàng thông báo thường đến 07:00 theo múi giờ người nhận. Giữ thời điểm hoàn tiền trong trạng thái yêu cầu để khách vẫn tra cứu được. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Ghi `unsupported_input_received` khi đầu vào là audio, kèm `trace_id`. Theo dõi số yêu cầu audio chưa chuyển được sang văn bản hoặc nhân viên sau 24 giờ. Cảnh báo nếu có từ 1 ca/ngày. | Chỉ rõ cách gửi lại bằng chữ và cung cấp nút chuyển nhân viên để khách có phương án tiếp tục ngay. | Quản lý sản phẩm trợ lý hoàn phí |
| 5 | Ngầm | Mỗi ngày đối soát toàn bộ đơn có mã giảm giá bằng `trace_id`, số tiền đã thu sau giảm và số tiền hoàn thực tế. Ghi `refund_discount_reconciliation_failed` khi lệch trên 0 đ so với mức chính sách. | Tính tiền hoàn từ dữ liệu đã thu sau giảm do sổ cái cung cấp. Chuyển mọi ca lệch vào hàng đợi đối soát để kế toán xác minh và xử lý. | Kế toán trưởng |
