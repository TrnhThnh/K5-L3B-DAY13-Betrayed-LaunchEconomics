# Báo cáo nhóm

Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Betrayed
- Lớp: L3B
- Thành viên: 2 người, xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm trả lời bốn câu hỏi cho trợ lý hoàn phí của LogiX-VN: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot phải thiết kế thế nào để ra được quyết định.
Mọi phép tính nằm trong [lab13.py](../../src/lab13.py), chạy trong `src/` trên 1.624 lần chạy của 1.200 yêu cầu (dữ liệu giả lập).
Số của nhiệm vụ trước được dùng lại cho nhiệm vụ sau: chi phí theo loại chọn phạm vi pilot, bảng độ nhạy chọn rủi ro, tỉ lệ trong đợt chạy thử làm căn cứ cho ngưỡng dừng.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Mô hình chi phí | Qua ba phép thử đáp án biết trước, rồi cộng chi phí mọi lần chạy và chỉ chia cho yêu cầu thành công; tách theo loại và cộng chi phí cố định | [bang_chi_phi.md](bang_chi_phi.md) |
| B · Độ nhạy | Đổi từng yếu tố và một cặp; tính chi phí cả hệ thống theo giới hạn chạy và kịch bản xem lại 100% | [bang_chi_phi.md](bang_chi_phi.md) |
| C · Bảng lỗi | Có 20 nhãn tham khảo và bảng khắc phục 5 loại; chờ hai bộ nhãn độc lập để tính đồng thuận | [bang_loi.md](bang_loi.md) |
| D · Pilot | Tính năm cỡ mẫu trước khi chọn chia theo nhân viên; đặt ngưỡng dừng sau khi xem tỉ lệ của đợt chạy thử | [pilot_plan.yaml](pilot_plan.yaml) |
| E · Chỉ số và hồ sơ | Tính thử ba chỉ số, đặc tả 12 event có `trace_id`, ba dòng rủi ro và hồ sơ launch bảy mục | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

| Nội dung | Con số chính |
| --- | --- |
| Chi phí mỗi việc thành công | 4.472 đ (simulated), gấp 16,3 lần hoá đơn token và tool mỗi yêu cầu |
| Yếu tố nhạy nhất | Số ca làm lại gấp đôi: +51,8% (simulated); giá token gấp đôi chỉ +5,6% (simulated) |
| So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× 12.000 đ, chưa gồm cố định (simulated) |
| Giới hạn chạy lại | 2 lần rẻ nhất cho công ty (6.901.220 đ); 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ) (simulated) |
| Xem lại 100% trong phạm vi | 11.743 đ = 0,98×, hoặc 12.414,50 đ = 1,03× nếu làm lại 15,3 phút (simulated) |
| Chỉ số trong đợt chạy thử | Chính 82,83%; bỏ qua gợi ý 27,12%; mở lại trong 7 ngày 4,25% |
| Pilot | `noi_dia` và `hang_nang`, 20 + 20 nhân viên, 859 yêu cầu hiệu dụng mỗi nhóm, mức chênh 6 điểm, quyết định 12/01/2027 |

**Đề xuất:** Go có điều kiện, với năm điều kiện có người phụ trách và ngày kiểm tra trong [hồ sơ launch v0](ho_so_launch_v0.md).

**Kết quả duyệt chéo nhận từ hội đồng:** chờ điền theo phiếu thật của hội đồng.

## 5. Khó khăn và cách xử lý

| Khó khăn | Cách xử lý |
| --- | --- |
| Nhóm chỉ có 2 người cho bốn vai | Mỗi người giữ nhiều vai và bàn giao qua repo theo bảng chia việc trong `TEAM.md` |
| Trên Windows, `python lab13.py` báo `UnicodeEncodeError: 'charmap' codec can't encode character 'ử'` khi output được chuyển ra file hoặc pipe | Thêm `sys.stdout.reconfigure(encoding='utf-8')`; chạy lại với output chuyển ra file kết thúc bình thường |
| Lệnh kiểm tra YAML trong `CHECKPOINTS.md` báo `UnicodeDecodeError` trên Windows | Mở file với `encoding='utf-8'` |
| Với 40 nhân viên, không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm | Chia theo nhân viên, chấp nhận mức chênh 6 điểm và ghi rõ power 0,64 ở 5 điểm |
| `hang_nang` kém hơn hẳn mức trung bình trong phạm vi: làm lại 11,39%, xem lại 100% bằng 1,22× (simulated) | Thêm cổng ngày 21/12: loại còn làm lại trên 7% rút khỏi pilot; chỉ còn `noi_dia` vẫn đủ mẫu |
| Chỉ số chính trong phạm vi đã là 92,26%, xa mức nền cho sẵn 70% | Đo mức nền ở đối chứng tuần 1 và tính lại power tại cổng trước khi đo chính thức |

## 6. Tổng hợp đóng góp

- Trịnh Hưng Thịnh: nhiệm vụ A và B.
- Lưu Nguyễn Chí Đức: kiểm số A–B, nhiệm vụ D và E, báo cáo nhóm.
- Cả hai: nhiệm vụ C, duyệt chéo và nộp bài.

Chi tiết và bằng chứng nằm trong [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

- Đợt chạy thử không có nhóm đối chứng, nên các chỉ số không cho biết tác động của trợ lý.
- Phút xem lại và làm lại là simulated; cần đo thật bằng event từ tuần đầu rồi tính lại chi phí.
- ICC 0,02 là giả định cho sẵn, chưa đo; cần ước lượng lại từ dữ liệu nhóm đối chứng.
- Mẫu chỉ có 20 `staff_id` ở 6 depot (đếm trên `logix_requests.csv`), trong khi kế hoạch pilot dùng 40 nhân viên ở 12 depot.
- Pilot chỉ đủ mẫu cho mức chênh 6 điểm, nên có 36% khả năng bỏ lỡ tác động thật 5 điểm.

## 8. Tài liệu tham khảo

- [Hướng dẫn chi tiết buổi chiều](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- [Dữ liệu, số liệu dùng chung và công thức](../../docs/du_lieu_va_cong_thuc.md).
- [Đề bài Lab 13](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx).
- [Slide Launch & Economics](../../docs/Ngay13_Slide_Launch_Economics.pdf).
- statsmodels, `statsmodels.stats.power.NormalIndPower`.
