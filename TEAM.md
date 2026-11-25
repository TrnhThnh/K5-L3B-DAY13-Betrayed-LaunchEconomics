# Team

<!-- markdownlint-disable MD024 : mẫu của lab lặp lại ba mục con cho từng thành viên -->

## Thông tin nhóm

- Tên nhóm: Betrayed
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Betrayed-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: <https://github.com/TrnhThnh/K5-L3B-DAY13-Betrayed-LaunchEconomics>, nhánh `main`, commit cuối trên `main` trước 23h59 GMT+7 ngày 25/11/2026

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | --- | --- | --- | --- | --- |
| 1 | Chờ bổ sung | Chờ bổ sung | Chờ bổ sung | TrnhThnh | Người viết code A–B, người gắn nhãn 1 |
| 2 | Lưu Nguyễn Chí Đức | 2A202603923 | Chờ bổ sung | TheDLCrimson | Người kiểm số A–B, người viết code D1, người gắn nhãn 2 kiêm giữ hồ sơ |

Nhóm có 2 người nên mỗi người giữ nhiều vai trong bốn vai của lab.
Người viết code đổi từ thành viên 1 (A–B) sang thành viên 2 (D1), nên cả hai đều làm việc trực tiếp với mô hình trong `src/lab13.py`.

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

## Chia việc

| Phần | Phụ trách | Sản phẩm và bàn giao |
| --- | --- | --- |
| A–B | TrnhThnh | A1–A4, B1–B4 trong [lab13.py](src/lab13.py) và [bảng chi phí](report/team/bang_chi_phi.md); bàn giao số A3–A4, B1–B4 để chọn phạm vi, ngưỡng chi phí và rủi ro |
| Kiểm số A–B | Đức | Chạy lại trên máy thứ hai và đối chiếu một dòng chi phí |
| C | Cả hai | Mỗi người ghi riêng 20 nhãn; Đức tổng hợp vào [bảng lỗi](report/team/bang_loi.md); hai người tính đồng thuận, thống nhất ca lệch và chọn 5 ca khắc phục |
| D | Đức | Phép tính D1 trong [lab13.py](src/lab13.py) và [kế hoạch pilot](report/team/pilot_plan.yaml) |
| E | Đức | [Chỉ số, event, rủi ro](report/team/chi_so.md) và [hồ sơ launch v0](report/team/ho_so_launch_v0.md) |
| Duyệt chéo, báo cáo và nộp | Cả hai | Đức tổng hợp [báo cáo nhóm](report/team/group_report.md) và [phiếu chấm](report/team/phieu_cham.md); TrnhThnh rà bằng chứng chi phí và trình bày A–B; mỗi người tự điền báo cáo cá nhân và tự nộp link repo trên LMS |

## Cá nhân

## TrnhThnh (chờ bổ sung họ tên và MSSV)

### Phần việc phụ trách

- Nhiệm vụ A và B: mô hình chi phí và bảng độ nhạy.
- Gắn nhãn 20 ca lỗi (người gắn nhãn 1).
- Rà bằng chứng chi phí và trình bày A–B khi duyệt chéo.

### Đóng góp cụ thể

- Viết A1–A4 và B1–B4 trong `src/lab13.py`.
- Điền `report/team/bang_chi_phi.md`.
- Lập bảng chia việc ban đầu của nhóm.
- Codex hỗ trợ triển khai và kiểm tra A–B theo hướng dẫn trong repo.

### Bằng chứng

- Commit `8db1bd7`: [lab13.py](src/lab13.py), [bang_chi_phi.md](report/team/bang_chi_phi.md), `TEAM.md`.

## LuuNguyenChiDuc-2A202603923

### Phần việc phụ trách

- Kiểm số A–B.
- Nhiệm vụ D (cỡ mẫu và kế hoạch pilot) và E (chỉ số, event, rủi ro, hồ sơ launch v0).
- Gắn nhãn 20 ca lỗi (người gắn nhãn 2) và tổng hợp bảng lỗi.
- Tổng hợp báo cáo nhóm và phiếu chấm.

### Đóng góp cụ thể

- Chạy lại `src/lab13.py` trên máy thứ hai: ba phép thử A1 đạt, số A–B khớp số đối chiếu trong hướng dẫn.
- Chốt chia pilot theo nhân viên với mức chênh 6 điểm và đề xuất Go có điều kiện.
- Hoàn thành phần tính D1 và E1 trong `src/lab13.py`, `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md`.
- Sửa lỗi in tiếng Việt khi chuyển hướng output trên Windows.
- Bổ sung kết luận A3 trong `bang_chi_phi.md`; hoàn thiện `TEAM.md` theo mẫu và viết báo cáo nhóm.

### Bằng chứng

- Commit `438292a`: [lab13.py](src/lab13.py), [pilot_plan.yaml](report/team/pilot_plan.yaml), [chi_so.md](report/team/chi_so.md), [ho_so_launch_v0.md](report/team/ho_so_launch_v0.md).
- Con số chính: cần 859 yêu cầu mỗi nhóm cho mức chênh 6 điểm; power 0,64 nếu tác động thật là 5 điểm; xem lại 100% riêng `hang_nang` bằng 1,22× chi phí nhân viên (simulated).
