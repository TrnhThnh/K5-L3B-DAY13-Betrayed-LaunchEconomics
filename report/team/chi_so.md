# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py`.
Số tính từ cột `_simulated` ghi nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) |
| Dùng (đề xuất thêm) | Độ sâu: % yêu cầu trong phạm vi của nhóm trợ lý mà nhân viên mở gợi ý | Số `trace_id` có `agent_suggestion_opened`, chia số `refund_request_created` có `arm` là trợ lý | Không cần tính |
| An toàn (đề xuất thêm) | % đơn hoàn sai tiền qua kiểm tra mẫu 100 đơn mỗi tuần | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm | Không cần tính |

Chỉ số trong đợt chạy thử theo phạm vi:

| Nhóm | Chính | Bỏ qua gợi ý | Mở lại 7 ngày | Làm lại |
| --- | ---: | ---: | ---: | ---: |
| Trong phạm vi | 92,26% (906/982) | 21,09% (27/128) | 3,97% (39/982) | 4,89% (48/982) |
| `noi_dia` | 95,27% (785/824) | 18,28% (17/93) | 3,16% (26/824) | 3,64% (30/824) |
| `hang_nang` | 76,58% (121/158) | 28,57% (10/35) | 8,23% (13/158) | 11,39% (18/158) |

Đợt chạy thử không có nhóm đối chứng, nên các số này chỉ mô tả đợt chạy thử và không cho biết tác động của trợ lý.

## Danh sách event

`trace_id` được tạo khi yêu cầu được tạo, cho cả hai nhóm, và nối mọi event theo yêu cầu. Mỗi event có thời điểm phát sinh; mỗi lần chạy có thêm run_id để nối trace chi tiết.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm, trace_id | Khi khách gửi |
| `agent_run_completed` | Agent | run_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_opened` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi nhân viên mở gợi ý |
| `staff_review_decision` | Giao diện nhân viên | quyet_dinh (giu, sua, bo), phut_xem_lai đo thật, trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Giao diện nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `refund_notice_sent` | Dịch vụ thông báo | noi_dung_trang_thai, so_tien, trace_id | Khi gửi tin cho khách |
| `ticket_closed` | Hệ thống ticket | closed_at, closed_by, phut_xu_ly đo thật, trace_id | Khi đóng, cả hai nhóm |
| `ticket_reopened` | Hệ thống ticket | reopened_at, ly_do, trace_id | Khi khách mở lại |
| `refund_amount_reconciled` | Dịch vụ đối soát | so_tien_da_hoan, so_tien_dung, policy_version, ket_qua, trace_id | Mỗi ca hoàn, trước khi khóa dữ liệu tuần |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo:** mỗi chỉ số và luật dừng đều tính được từ event.

| Chỉ số hoặc luật | Event dùng để tính |
| --- | --- |
| Chỉ số chính | `refund_request_created`, `ticket_closed`, `ticket_reopened` |
| Bỏ qua gợi ý | `staff_review_decision` |
| Lỗi lọt đến khách, kể cả riêng `hang_nang` | `refund_request_created`, `ticket_closed`, `ticket_reopened`. Đếm mỗi yêu cầu một lần trên cohort đủ theo dõi; luật dừng an toàn còn xem hằng ngày số ca mở lại đã quan sát. |
| Độ sâu | `refund_request_created`, `agent_suggestion_opened` |
| Hoàn sai tiền | `audit_sample_checked` |
| Hoàn trùng, báo đã hoàn khi sổ cái không ghi | `refund_ledger_write`, `refund_notice_sent` |
| Tỉ lệ làm lại | `refund_request_created`, `staff_rework_completed` |
| Chi phí mỗi việc thành công | `agent_run_completed`, `staff_review_decision`, `staff_rework_completed`, `ticket_closed`, `ticket_reopened`, `handoff_to_staff`, `refund_amount_reconciled`. Tử số gồm mọi lượt chạy và phút xử lý của trợ lý. Mẫu số gồm các ca trợ lý đóng, không chuyển nhân viên, không mở lại trong 7 ngày và đúng tiền. |
| Chi phí nhân viên tự làm (thay giả định 6 phút) | `ticket_closed.phut_xu_ly` của nhóm đối chứng |
| Ca chuyển nhân viên | `handoff_to_staff`, `ticket_closed.phut_xu_ly` |

## E2 · Rủi ro kinh tế

Mức gốc: 4.472 đ/việc thành công trên toàn mẫu, 3.414 đ trong phạm vi (simulated).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ; trong phạm vi lên 5.147 đ (simulated) | Làm lại 7 ngày > 7% (đợt chạy thử trong phạm vi 4,89%) | Giữ mức xem lại, rà 20 trace làm lại; loại còn trên 7% ngày 21/12 rút khỏi pilot | PM trợ lý hoàn phí |
| Xem lại gấp đôi, hoặc phải xem lại 100% kéo dài | Gấp đôi: +40,7%, lên 6.292 đ. Xem lại 100%: 11.743 đ = 0,98×, hoặc 12.414,50 đ = 1,03× nếu làm lại 15,3 phút (simulated) | Trên 50% yêu cầu còn được xem lại vào ngày 21/12; phút mỗi lượt xem lại > 5,1 (ngưỡng hoà vốn, simulated) | Không mở rộng; đo lý do sửa và bỏ, rút ngắn thao tác xem lại | Trưởng nhóm CSKH |
| Khối lượng thấp làm chi phí cố định 40 triệu đ/tháng nặng hơn | Cố định mỗi việc: 1.185 đ ở 45.000 yêu cầu/tháng, 2.370 đ ở một nửa, 11.852 đ ở bước 0,10 (simulated) | Việc thành công theo tuần dưới 50% kế hoạch; khối lượng dưới 6.212 yêu cầu/tháng (simulated) | Không kéo dài bước 0,10; xem lại hợp đồng chi phí cố định trước khi mở rộng | Giám đốc vận hành LogiX-VN |
