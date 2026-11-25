# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: Betrayed · Lớp: L3B

**Phạm vi đề xuất:** pilot cho `noi_dia` và `hang_nang`.
Loại `quoc_te` (1,88× chi phí nhân viên, simulated; thành công 27,3%) và `doi_tac` (0,85×, simulated; thành công 54,4%; có điều khoản riêng).
Số chạy thử lấy từ mẫu 1.200 yêu cầu **không có nhóm đối chứng**; tính bằng `src/lab13.py`.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (simulated), gấp 16,3 lần hoá đơn token và tool mỗi yêu cầu (274,65 đ). Trong phạm vi 3.414 đ; cộng cố định 4.599 đ ở 45.000 yêu cầu/tháng, 5.784 đ ở một nửa (simulated) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại ×2: +51,8% (6.787 đ). Tỉ lệ xem lại ×2: +40,7% (6.292 đ). Lương +25%: +23,1% (5.506 đ). Giá token ×2 chỉ +5,6% (simulated) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm (12.000 đ) | Cả hệ thống, gồm ca chuyển nhân viên: toàn mẫu 5.865 đ/yêu cầu = 0,49× (chưa gồm cố định). Trong phạm vi, gồm cố định: 5.217 đ = 0,43× ở 45.000 yêu cầu/tháng; 6.303 đ = 0,53× ở một nửa (simulated) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, dùng, an toàn | Chỉ số trong đợt chạy thử: đóng trong 24 giờ và không mở lại **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại trong 7 ngày **4,25%** (51/1.200). Trong phạm vi: 92,26% · 21,09% · 3,97% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Chưa có: đang chờ hai bộ nhãn độc lập của 20 ca và tỉ lệ đồng thuận (`bang_loi.md`) | Chưa | PM trợ lý hoàn phí |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, 20 + 20; cần 859 yêu cầu/nhóm cho mức chênh 6 điểm, hệ số thiết kế 6,96, từ 299 yêu cầu/người. Đo 21/12/2026 đến 03/01/2027, quyết định 12/01/2027, 5 luật dừng (`pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100% trong phạm vi: 11.743 đ = 0,98×; làm lại 15,3 phút thì 12.414 đ = 1,03×. Riêng `hang_nang`: 14.699 đ = 1,22× (simulated) | Giả lập | Trưởng nhóm CSKH |

## Con số bất lợi và cách xử lý

| Con số bất lợi | Cách xử lý |
| --- | --- |
| Power chỉ **0,64** nếu tác động thật là 5 điểm | Giám đốc vận hành ký chấp nhận trước khi bốc thăm; không đạt ngưỡng thì không mở rộng, không kéo dài để tìm ý nghĩa thống kê |
| Bước 0,10 (4 người, xem lại 100%, gồm cố định): **23.595 đ = 1,97×** (simulated) | Chỉ giữ một tuần để kiểm an toàn, coi là chi phí của pilot |
| `hang_nang`: làm lại **11,39%** (18/158), mở lại **8,23%** (13/158) | Ngày 21/12 loại nào làm lại 7 ngày > 7% thì rút khỏi pilot. Chỉ còn `noi_dia` vẫn đủ mẫu (cỡ mẫu hiệu dụng 880 ≥ 859) |
| Chỉ số chính trong phạm vi đã là **92,26%**, xa mức nền cho sẵn 70% | Không viết trợ lý đã nâng chỉ số. Đo mức nền ở nhóm đối chứng tuần 1; từ 94% trở lên thì dừng tại cổng vì không còn chỗ cho 6 điểm |
| Phút xem lại và làm lại là **simulated** | Đo thật bằng event từ tuần 1 và tính lại bảng chi phí ngày 14/12 |

## Điều kiện

| # | Điều kiện và ngưỡng | Người phụ trách | Ngày kiểm tra |
| --: | --- | --- | --- |
| 1 | Khoá chống trùng và đối soát sổ cái hằng giờ chạy được; bộ test có 0 ca hoàn trùng, 0 tin "đã hoàn" thiếu bản ghi sổ cái | Kỹ sư trưởng agent | 04/12/2026 |
| 2 | Ký chấp nhận mức chênh 6 điểm (power 0,64 ở 5 điểm), seed bốc thăm và ngày quyết định | Giám đốc vận hành LogiX-VN | 04/12/2026 |
| 3 | 100% yêu cầu của một ngày test có đủ event kèm `trace_id` | PM trợ lý hoàn phí | 04/12/2026 |
| 4 | Từ 95% ca xem lại có phút đo thật; bảng chi phí được tính lại | PM trợ lý hoàn phí | 14/12/2026 |
| 5 | Chỉ giảm xem lại cho loại có làm lại 7 ngày ≤ 7%; loại còn trên 7% rút khỏi pilot | Trưởng nhóm CSKH | 14/12 và 21/12/2026 |

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang` theo 5 điều kiện trên; trượt điều kiện 1, 2 hoặc 3 thì lùi ngày bắt đầu 07/12/2026, chưa cho nhân viên dùng trợ lý.
