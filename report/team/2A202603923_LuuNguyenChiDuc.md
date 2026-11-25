# Báo cáo cá nhân - 2A202603923 - Lưu Nguyễn Chí Đức

## 1. Thông tin thành viên

- Họ tên: Lưu Nguyễn Chí Đức
- MSSV: 2A202603923
- Email: <26ai.duclnc@vinuni.edu.vn>
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người kiểm số A–B, người viết code D1, người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Kiểm số nhiệm vụ A và B.
- Nhiệm vụ D: cỡ mẫu theo ba cách chia và kế hoạch pilot.
- Nhiệm vụ E: đặc tả chỉ số, event, rủi ro kinh tế và hồ sơ launch v0.
- Nhiệm vụ C: tổng hợp bảng lỗi (phần gắn nhãn độc lập chưa thực hiện).
- Tổng hợp báo cáo nhóm và phiếu chấm.

## 3. Đóng góp cụ thể

- Chạy lại `src/lab13.py` trên máy thứ hai: ba phép thử A1 đạt, số A–B khớp số đối chiếu trong hướng dẫn.
- Đối chiếu dòng làm lại bằng phép tính riêng: 1.132 phút × 2.000 đ = 2.264.000 đ (simulated), khớp bảng A2.
- Chốt chia pilot theo nhân viên (20 + 20) với mức chênh 6 điểm, chấp nhận power 0,64 ở mức 5 điểm.
- Chốt đề xuất Go có điều kiện cho phạm vi `noi_dia` và `hang_nang`.
- Hoàn thành phần tính D1 và E1 trong `src/lab13.py`, `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md`.
- Sửa lỗi in tiếng Việt khi chuyển hướng output trên Windows.
- Bổ sung kết luận A3 trong `bang_chi_phi.md`; hoàn thiện `TEAM.md` và báo cáo nhóm.
- Tổng hợp `bang_loi.md` (nhãn nhóm nhận dùng, quy tắc cho ca dễ lẫn, ghi rõ nguồn nhãn) và chỉnh lại mẫu năm luật dừng.

## 4. Bằng chứng

- Commit `438292a` (25/11/2026): `src/lab13.py`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
- Commit `3301706` (25/11/2026): năm luật dừng trong `pilot_plan.yaml`, bản tổng hợp `bang_loi.md` và cập nhật các báo cáo.
- D1: 1.251 yêu cầu mỗi nhóm nếu chia theo yêu cầu; 3.103 nếu chia theo nhân viên với m = 75; trần 1.000 (20 nhân viên) và 300 (6 depot); ít nhất 299 yêu cầu mỗi người cho mức chênh 6 điểm.
- E1: chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại trong 7 ngày 4,25% (51/1.200).
- Rủi ro: làm lại gấp đôi đưa chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ (simulated).

## 5. Công cụ AI đã dùng

Tôi dùng Claude Code (model Claude Sonnet 5.5) làm trợ lý, theo bốn kiểu việc.

| Kiểu việc | AI làm gì | Cách kiểm tra |
| --- | --- | --- |
| Soạn thảo | Soạn phần tính D1 và E1 trong `lab13.py`, `pilot_plan.yaml`, `chi_so.md`, hồ sơ launch, báo cáo và bản tổng hợp bảng lỗi | Tôi chốt cách chia pilot và đề xuất trước khi soạn phần D, E; tôi tự commit và push |
| Phản biện | Chỉ ra điểm yếu của kế hoạch và bài nhóm: `hang_nang` kém hơn mức trung bình, mức nền 92,26% xa 70%, bước 0,10 tốn 1,97× (simulated), kết luận A3 còn thiếu, mệnh đề KHÔNG THÌ chưa nêu việc bị cấm | Các con số làm căn cứ đều in ra từ `lab13.py`, nên chạy lại được |
| Tra cứu | Đọc đề, rubric, hướng dẫn và slide về cỡ mẫu và luật dừng | Công thức cỡ mẫu theo `docs/du_lieu_va_cong_thuc.md`; statsmodels cho 1.249,6, khớp 1.251 trong sai số 2% |
| Kiểm tra | Chạy `lab13.py` trên máy tôi, đối chiếu số A–B với hướng dẫn, kiểm tự động YAML, từ bị cấm và nguồn của từng con số | Ba phép thử đáp án biết trước đạt; dòng làm lại tính riêng khớp 2.264.000 đ (simulated) |

## 6. Tự đánh giá

Tôi làm phần D và E sau khi Thịnh bàn giao số A–B, và chốt chia pilot theo nhân viên cùng đề xuất Go có điều kiện.
Tôi chấp nhận đánh đổi mức chênh 6 điểm thay vì 5: nếu tác động thật chỉ là 5 điểm thì power còn 0,64, nên con số này được ghi thẳng trong hồ sơ.
Ngưỡng dừng được đặt sau khi xem tỉ lệ của đợt chạy thử, để pilot không bị dừng ngay chỉ vì mức hiện tại.
Gần hạn nộp, bảng lỗi có hai phiên bản khác nhau; tôi giữ bản ghi rõ nguồn nhãn và không báo tỉ lệ đồng thuận chưa đo.

Điều chưa làm được và tôi sẽ làm khác:

- Phần C không có hai bộ nhãn độc lập; lần sau gắn nhãn tay ngay ở CP3, trước khi mở đáp án.
- Hai người cùng sửa một file nên bị xung đột khi pull; lần sau chia rõ ai sửa file nào và hẹn giờ bàn giao từ đầu buổi.
