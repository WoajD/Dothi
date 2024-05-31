from do_thi import DoThi

g = DoThi()
g.doc_mtk("path.txt")

print("Danh sach canh:")
g.InDSC()

print("Danh sanh ke")
g.in_dsk()

if g.vo_huong():
    tongBac = g.TongBac()
    print(f"Tổng bậc của đồ thị: {tongBac}")
    bacDinh1 = g.Bac(1)
    print(f"Bậc của đỉnh 1: {bacDinh1}")
else:
    tongBanBacRa = g.TongBanBacRa()
    tongBanBacVao = g.TongBanBacVao()
    print(f"Tổng bán bậc ra: {tongBanBacRa}")
    print(f"Tổng bán bậc vào: {tongBanBacVao}")
    x1 = g.BanBacRa(2)
    x2 = g.BanBacVao(2)
    print(f"Bán bậc ra của đỉnh 2: {x1}")
    print(f"Bán bậc vào của đỉnh 2: {x2}")
if g.DayDu():
    print("Đồ thị đầy đủ")
if g.Vong():
    print("Đồ thị vòng")
if g.HaiPhia():
    print("Đồ thị hai phía")