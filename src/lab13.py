"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a).

Chạy trong src/ bằng python lab13.py. Hai file CSV là dữ liệu giả lập.
Mô hình A–B dựa trên docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000
KHOI_LUONG_THANG = 45_000
PHAM_VI = ('noi_dia', 'hang_nang')


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k == 0:
        return 0
    if p == 0:
        return math.inf if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    if p == 1:
        return float(k > 0)
    return -math.expm1(k * math.log1p(-p))


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    xac_suat = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / xac_suat if xac_suat else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        # Ca vượt giới hạn chuyển thẳng cho nhân viên, tính riêng ở B3.
        reqs = reqs[reqs['so_lan_chay'] <= max_lan_chay]

    tien_token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())
    return dict(
        token=token, tool=tool,
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
        thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else math.inf,
    )


def in_nhiem_vu_a(runs, reqs, goc):
    print('\nA2 | Chi phí từ trace')
    nhan_simulated = {'xem_lai', 'lam_lai', 'tong', 'cps'}
    for ten, gia_tri in goc.items():
        nhan = ' [simulated]' if ten in nhan_simulated else ''
        print(f'{ten:12s} {gia_tri:>14,.2f}{nhan}')
    hoa_don = (goc['token'] + goc['tool']) / len(reqs)
    print(f'Hóa đơn/yêu cầu: {hoa_don:,.2f} đ, CPS gấp {goc["cps"] / hoa_don:.2f} lần [simulated]')
    print(f'Làm lại chiếm {goc["lam_lai"] / goc["tong"]:.2%} [simulated]')
    ca_khong_thanh_cong = len(reqs) - goc['thanh_cong']
    ca_he_thong = goc['tong'] + BASELINE * ca_khong_thanh_cong
    print(f'Cả hệ thống/yêu cầu: {ca_he_thong / len(reqs):,.2f} đ [simulated]')

    print('\nA3 | Loại | Yêu cầu | Thành công | Lần chạy/YC | CPS [simulated] | Bội số [simulated]')
    for loai, nhom in reqs.groupby('loai'):
        chi_phi = mo_hinh(runs, nhom)
        print(f'{loai:9s} | {len(nhom):4} | {chi_phi["thanh_cong"] / len(nhom):6.1%} | '
              f'{nhom["so_lan_chay"].mean():.2f} | {chi_phi["cps"]:,.2f} | {chi_phi["cps"] / BASELINE:.2f}x')
    runs_quoc_te = runs[runs['request_id'].isin(reqs.loc[reqs['loai'].eq('quoc_te'), 'request_id'])]
    ti_le_ok = runs_quoc_te['status'].eq('ok').groupby(runs_quoc_te['attempt']).mean()
    print('Quốc tế, tỉ lệ ok theo lần:', ', '.join(f'{lan}: {ti_le:.1%}' for lan, ti_le in ti_le_ok.items()))

    trong_pham_vi = reqs[reqs['loai'].isin(PHAM_VI)]
    chi_phi = mo_hinh(runs, trong_pham_vi)
    # Quy mô tháng là tổng yêu cầu, tính số thành công trong phạm vi trên cả mẫu 1.200.
    ti_le = chi_phi['thanh_cong'] / len(reqs)
    print('\nA4 | Yêu cầu/tháng | Thành công | Cố định/việc | CPS + cố định [simulated] | Bội số [simulated]')
    for khoi_luong in (KHOI_LUONG_THANG, KHOI_LUONG_THANG // 2):
        thanh_cong = khoi_luong * ti_le
        co_dinh = CHI_PHI_CO_DINH / thanh_cong
        cps = chi_phi['cps'] + co_dinh
        print(f'{khoi_luong:,} | {thanh_cong:,.0f} | {co_dinh:,.2f} | {cps:,.2f} | {cps / BASELINE:.2f}x')
    hoa_von = CHI_PHI_CO_DINH / (ti_le * (BASELINE - chi_phi['cps']))
    print(f'Hòa vốn theo CPS tại {hoa_von:,.2f} yêu cầu/tháng [simulated]')


def in_nhiem_vu_b(runs, reqs, goc):
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA),
        'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=1.25 * LUONG_PHUT),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    print('\nB1 | Kịch bản | CPS [simulated] | Thay đổi [simulated]')
    thay_doi = {}
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        thay_doi[ten] = cps / goc['cps'] - 1
        print(f'{ten:25s} | {cps:,.2f} | {thay_doi[ten]:+.1%}')

    cap = mo_hinh(runs, reqs, **kich_ban['Giá token gấp đôi'], **kich_ban['Xem lại gấp đôi'])
    print(f'\nB2 | Token và xem lại gấp đôi: {cap["cps"]:,.2f} đ ({cap["cps"] / goc["cps"] - 1:+.1%}) [simulated]')
    # Với ba cặp tăng/giảm, kịch bản tăng cho mức thay đổi tuyệt đối lớn hơn.
    yeu_to = ('Giá token gấp đôi', 'Xem lại gấp đôi', 'Làm lại gấp đôi',
              'Lương tăng 25%', 'Tối đa 2 lần chạy', 'Chỉ 1 lần chạy')
    xep_hang = sorted(yeu_to, key=lambda ten: abs(thay_doi[ten]), reverse=True)
    print('Ba yếu tố nhạy nhất:', ', '.join(xep_hang[:3]))

    print('\nB3 | Giới hạn | Chi phí trợ lý [simulated] | Ca không thành công | Cả hệ thống [simulated] | CPS [simulated]')
    for gioi_han in (1, 2, 3):
        chi_phi = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - chi_phi['thanh_cong']
        ca_he_thong = chi_phi['tong'] + BASELINE * khong_thanh_cong
        print(f'{gioi_han} | {chi_phi["tong"]:,.2f} | {khong_thanh_cong} | {ca_he_thong:,.2f} | {chi_phi["cps"]:,.2f}')

    trong_pham_vi = reqs[reqs['loai'].isin(PHAM_VI)]
    chi_phi = mo_hinh(runs, trong_pham_vi)
    runs_ok = runs[runs['request_id'].isin(trong_pham_vi['request_id']) & runs['status'].eq('ok')]
    so_ca_xem = runs_ok['request_id'].nunique()
    ca_lam_lai = reqs['ket_qua'].eq('lam_lai')
    so_ca_lam_lai = trong_pham_vi['ket_qua'].eq('lam_lai').sum()
    phut_lam_lai_tb = reqs.loc[ca_lam_lai, 'phut_lam_lai_simulated'].mean()
    print(f'\nB4 | {so_ca_xem} ca xem lại, {so_ca_lam_lai} ca làm lại, {chi_phi["thanh_cong"]} thành công')
    for phut_lam_lai in (9, phut_lam_lai_tb):
        khong_xem_lai = chi_phi['token'] + chi_phi['tool'] + so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = khong_xem_lai + so_ca_xem * 5 * LUONG_PHUT
        cps = tong / chi_phi['thanh_cong']
        phut_hoa_von = (BASELINE * chi_phi['thanh_cong'] - khong_xem_lai) / (so_ca_xem * LUONG_PHUT)
        print(f'Làm lại {phut_lam_lai:.2f} phút/ca | Tổng {tong:,.2f} | CPS {cps:,.2f} = '
              f'{cps / BASELINE:.2f}x | Xem lại hòa vốn {phut_hoa_von:.2f} phút [simulated]')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    goc = mo_hinh(runs, reqs)
    in_nhiem_vu_a(runs, reqs, goc)
    in_nhiem_vu_b(runs, reqs, goc)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
