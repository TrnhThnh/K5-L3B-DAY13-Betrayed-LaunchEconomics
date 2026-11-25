# Bảng lỗi và cách khắc phục · Nhiệm vụ C

<!-- markdownlint-disable MD033 : khối thu gọn cho bảng nhãn tham khảo -->

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai cột nhãn nháp do AI điền

Codex điền cả hai cột theo cùng bộ nhãn tham khảo. Hai bản nháp trùng 20/20 do dùng chung nguồn, **không phải hai bộ nhãn do hai thành viên gắn độc lập**.
Cột “Nhãn thống nhất” là nhãn nhóm nhận dùng sau khi đối chiếu với tình huống trong đề.

| Ca | Nháp AI 1 | Nháp AI 2 | Trùng bản nháp? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** không tính, vì chưa có hai bộ nhãn độc lập của thành viên (ngưỡng của bài là 16/20).

## Quy tắc phân biệt cho các ca dễ lẫn

- Ca 6 và 9 là do người dùng: gốc lỗi là chọn sai mục hoặc nhập sai loại mã; việc trợ lý không gợi ý lại là chỗ cần cải thiện.
- Ca 8 là hệ thống, không phải ngầm: điều khoản không tồn tại hiện ra trong câu trả lời, dù số tiền đúng.
- Ca 12 là ngầm: kết quả đúng nên không ai nhận ra chi phí token gấp 3 lần suốt 3 tuần.
- Ca 13 là giới hạn hệ thống: câu hỏi nằm ngoài phạm vi, kể cả khi trợ lý xử lý giới hạn đó kém.
- Ca 20 là hệ thống, không phải do người dùng: gửi lại sau 10 phút là hành vi bình thường, lỗi ở lệnh hoàn thiếu khoá chống trùng.

<details>
<summary>Nhãn tham khảo và căn cứ cho 20 ca</summary>

| Ca | Nhãn tham khảo | Căn cứ trong tình huống |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu hai chữ số của tài khoản. |
| 2 | Hệ thống | Trợ lý dùng sai tham số bảng giá cho kiện 28 kg. |
| 3 | Ngữ cảnh | Tiền về ví đúng thiết kế, trong khi khách chờ tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | LogiX thiếu dữ liệu của chặng do hãng nước ngoài giao. |
| 5 | Ngầm | Khoản hoàn tính trên giá trước giảm chỉ bị phát hiện khi kiểm tra mẫu. |
| 6 | Do người dùng | Khách chọn luồng giao trễ cho yêu cầu về hàng bị vỡ. |
| 7 | Hệ thống | Trợ lý báo đã hoàn dù sổ cái chưa ghi thành công. |
| 8 | Hệ thống | Trợ lý dẫn một điều khoản không tồn tại trong chính sách. |
| 9 | Do người dùng | Khách nhập mã đơn sàn vào ô mã vận đơn. |
| 10 | Ngữ cảnh | Điều khoản bất khả kháng được áp dụng đúng, nhưng cam kết trên ứng dụng tạo kỳ vọng khác. |
| 11 | Giới hạn hệ thống | Trợ lý không hỗ trợ dạng đầu vào âm thanh. |
| 12 | Ngầm | Chi phí token tăng kéo dài dù kết quả đúng và chưa có ai phát hiện. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý. |
| 14 | Do người dùng | Khách bấm xác nhận nhận tiền trước khi tiền về. |
| 15 | Hệ thống | Trợ lý tính hoàn 100% thay vì 50% theo chính sách. |
| 16 | Ngữ cảnh | Giờ gửi đúng thiết kế gửi ngay, nhưng rơi vào giờ nghỉ của khách. |
| 17 | Ngầm | Bảng giá cũ gây sai tiền nhiều ngày mà khách không mở lại yêu cầu. |
| 18 | Ngữ cảnh | Số tiền đúng, nhưng thông báo thiếu cách tính nên khách hiểu là hoàn thiếu. |
| 19 | Giới hạn hệ thống | Yêu cầu vượt mốc 12 tháng dữ liệu trợ lý truy cập được. |
| 20 | Hệ thống | Luồng hoàn thiếu khóa chống trùng nên gửi lại yêu cầu dẫn đến hoàn hai lần. |

Đối chiếu với [hướng dẫn Lab 13, Nhiệm vụ C](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhiệm-vụ-c--bảng-lỗi-và-cách-khắc-phục-30-phút).

</details>

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Bảng dưới đây là phương án khắc phục đề xuất theo tình huống trong đề. Event và ngưỡng là đặc tả để triển khai và kiểm chứng trong pilot; các event báo lỗi bổ sung cho danh sách trong [chi_so.md](chi_so.md).

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi `refund_account_validation_failed` kèm `trace_id`, mã ngân hàng và lý do sai độ dài. Cảnh báo khi tỷ lệ lỗi này vượt 2% số lượt nhập tài khoản trong ngày. | Kiểm tra định dạng theo ngân hàng trước khi gọi tool hoàn tiền. Giữ yêu cầu ở trạng thái chờ và cho khách sửa thông tin. | Trưởng nhóm trải nghiệm khách hàng |
| 15 | Hệ thống | Trước khi gửi, đối chiếu số hoàn đề xuất với số hoàn tính từ thời gian giao trễ và phiên bản chính sách. Ghi `refund_policy_mismatch` với `trace_id` cho mọi trường hợp lệch trên 0 đ. | Chặn gửi khi số tiền lệch, chuyển người duyệt cùng cách tính theo chính sách và thêm ca biên 24–48 giờ vào bộ kiểm thử. | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Ghi `refund_notice_sent` kèm `trace_id`, múi giờ và giờ gửi địa phương. Kiểm tra mỗi ngày, cảnh báo nếu có bất kỳ thông báo thường nào gửi trong khoảng 22:00–07:00. | Xếp hàng thông báo thường đến 07:00 theo múi giờ người nhận. Giữ thời điểm hoàn tiền trong trạng thái yêu cầu để khách vẫn tra cứu được. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Ghi `unsupported_input_received` khi đầu vào là audio, kèm `trace_id`. Theo dõi số yêu cầu audio chưa chuyển được sang văn bản hoặc nhân viên sau 24 giờ. Cảnh báo nếu có từ 1 ca/ngày. | Chỉ rõ cách gửi lại bằng chữ và cung cấp nút chuyển nhân viên để khách có phương án tiếp tục ngay. | PM trợ lý hoàn phí |
| 5 | Ngầm | Mỗi ngày đối soát toàn bộ đơn có mã giảm giá bằng `trace_id`, số tiền đã thu sau giảm và số tiền hoàn thực tế. Ghi `refund_discount_reconciliation_failed` khi lệch trên 0 đ so với mức chính sách. | Tính tiền hoàn từ dữ liệu đã thu sau giảm do sổ cái cung cấp. Chuyển mọi ca lệch vào hàng đợi đối soát để kế toán xác minh và xử lý. | Kế toán trưởng |
