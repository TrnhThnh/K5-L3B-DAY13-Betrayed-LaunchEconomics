# Báo cáo cá nhân - 2A202603907 - Trịnh Hưng Thịnh

## 1. Thông tin thành viên

- Họ tên: Trịnh Hưng Thịnh
- MSSV: 2A202603907
- Email: <26ai.thinhth@vinuni.edu.vn>
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code A–B, người gắn nhãn 1

## 2. Phần việc phụ trách

- Nhiệm vụ A và B: mô hình chi phí và bảng độ nhạy.
- Nhiệm vụ C: gắn 20 nhãn.
- Rà bằng chứng chi phí và trình bày A–B khi duyệt chéo.

## 3. Đóng góp cụ thể

- Viết A1–A4 và B1–B4 trong `src/lab13.py`.
- Điền `report/team/bang_chi_phi.md`.
- Lập bảng chia việc ban đầu của nhóm.

## 4. Bằng chứng

- Commit `8db1bd7` (25/11/2026): `src/lab13.py`, `report/team/bang_chi_phi.md`, `TEAM.md`.
- A2: chi phí mỗi việc thành công 4.472 đ (simulated), gấp 16,3 lần hoá đơn token và tool mỗi yêu cầu.
- B3: giới hạn 2 lần chạy rẻ nhất cho cả hệ thống, 6.901.220 đ (simulated).

## 5. Công cụ AI đã dùng

Codex hỗ trợ triển khai và kiểm tra A–B theo hướng dẫn trong repo.

Kiểm chứng A–B với Codex: chạy ba phép thử A1 (1,20 · 1,25 · 1,25), sau đó tính lại chi phí theo từng giới hạn chạy từ CSV bằng một phép tính riêng. Kết quả khớp với mã A–B.

## 6. Tự đánh giá

- Kết quả A–B tái lập được từ hai file CSV. Dùng chi phí cả hệ thống khi chọn giới hạn chạy vì giới hạn một lần để lại thêm 85 ca cho nhân viên so với hai lần.
- Phần C đã có nhãn tham khảo và đề xuất khắc phục. Độ đồng thuận cần được xác nhận từ hai bộ nhãn độc lập.
