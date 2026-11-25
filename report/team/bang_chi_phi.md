# Bảng chi phí · Nhiệm vụ A và B

Tái lập số liệu bằng `python lab13.py` trong thư mục `src/`. Giá tính theo đồng Việt Nam. Nguồn phương pháp và giả định nằm trong [hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | Mọi lần chạy | đo từ trace |
| Tool | 84.000 đ | 5.600 lượt gọi | đo từ trace |
| Trong đó, token và tool của lần chạy thứ 2 và 3 | 93.804 đ | `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000 đ | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 đ | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 đ | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 đ | Tổng chi phí ÷ 978 | simulated |
| Hóa đơn token và tool chia cho số yêu cầu | 274,65 đ | (Token + tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hóa đơn trên mỗi yêu cầu (simulated). Tử số gồm cả chi phí các lần lỗi, còn mẫu số chỉ đếm 978 yêu cầu thành công.
- Làm lại chiếm **51,8%**, khoản lớn nhất trong tổng chi phí (simulated).
- Cộng 12.000 đ cho mỗi ca trong 222 ca không thành công theo quy ước B3, chi phí cả hệ thống là **5.865 đ/yêu cầu** (simulated), bằng 0,49 lần chi phí nhân viên tự làm.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Loại `quoc_te` tốn 22.515 đ/việc thành công (simulated), với 2,32 lượt chạy/yêu cầu mà chỉ thành công 27,3%. Tỉ lệ chạy `ok` lần 1, 2, 3 lần lượt là 30,0%, 11,4%, 2,2%, nên các lần chạy lại có hiệu quả thấp.

## A4 · Chi phí cố định cho phạm vi nội địa và hàng nặng

Khoản cố định là 40 triệu đ/tháng. Dùng 900 ca thành công trong phạm vi trên 1.200 yêu cầu toàn mẫu để quy đổi từ tổng lượng yêu cầu tháng.

| Khối lượng toàn hệ thống | Thành công trong phạm vi/tháng | Cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Cả hai mức vẫn dưới 12.000 đ/việc. Nếu giữ cơ cấu và hiệu suất của mẫu, chi phí mỗi việc thành công chạm 12.000 đ ở khoảng **6.212 yêu cầu/tháng** (simulated).

## B1 · Đổi từng yếu tố

Mức gốc là 4.472 đ/việc thành công (simulated).

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.314,50 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ/phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lượt sau lần 2, chuyển các yêu cầu vượt giới hạn cho nhân viên | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Bỏ lượt sau lần 1, chuyển các yêu cầu vượt giới hạn cho nhân viên | 4.111 đ | −8,1% |

Hai kịch bản giới hạn giữ chi phí token/tool của các lượt còn lại và tính 0 phút xem lại/làm lại cho ca chuyển thẳng do vượt giới hạn.

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi cho **6.543 đ/việc**, tăng **46,3%** (simulated), bằng tổng mức tăng riêng trước khi làm tròn.
- Ba yếu tố nhạy nhất trong các kịch bản đã thử lần lượt là số ca làm lại (**+51,8%**), tỉ lệ xem lại (**+40,7%**) và lương nhân viên (**+23,1%**), đều simulated.

## B3 · Chi phí cả hệ thống theo giới hạn chạy

Chi phí cả hệ thống trên 1.200 yêu cầu bằng tổng chi phí trợ lý cộng 12.000 đ cho mỗi ca không thành công.

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **Hai lần** rẻ nhất cho cả hệ thống (6.901.220 đ), còn **một lần** có chi phí mỗi việc thành công thấp nhất (4.111 đ), đều simulated. Giới hạn một lần để lại thêm 85 ca cho nhân viên so với giới hạn hai lần.

## B4 · Xem lại 100% câu trả lời trong phạm vi

Có 948 yêu cầu có lượt chạy `ok`, 48 ca làm lại và 900 ca thành công. Chi phí token và tool là 224.513 đ. Giả định mỗi lượt xem lại mất 5 phút.

- Theo giả định làm lại 9 phút/ca, chi phí là **11.743 đ/việc**, bằng 0,98× mức 12.000 đ (simulated). Dùng thời gian làm lại trung bình khoảng 15,3 phút/ca của toàn mẫu, chi phí tăng lên **12.414,50 đ/việc**, bằng 1,03× (simulated).
- Pilot cần đo tỷ lệ xem lại có thể giảm an toàn và số phút xem lại thực tế. Khi xem lại 100%, ngưỡng hòa vốn là khoảng **5,1 phút/lượt** nếu làm lại 9 phút, hoặc **4,8 phút/lượt** theo trung bình mẫu (simulated).
