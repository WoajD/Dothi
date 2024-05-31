class DoThi:
    def __init__(self):
        self.matrix = []
        self.dsk_list = []

    def doc_mtk(self, path):
        with open(path, 'r') as file:
            for line in file:
                self.matrix.append(list(map(int, line.strip().split())))
        self.convert_DSK()
    
    def convert_DSK(self):
        self.dsk_list = [[] for _  in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    self.dsk_list[i].append(j)

    def InDSC(self):
        for i in range(len(self.matrix)):
            for j in range(i, len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    print(f"Cạnh ({i}, {j})")

    def in_dsk(self):
        for i in range(len(self.dsk_list)):
            print(f"{i} : {self.dsk_list[i]}")

    def vo_huong(self):
        pass

    def TongBac(self):
        pass

    def Bac(self, dinh):
        pass

    def BanBacRa(self, dinh):
        pass

    def BanBacVao(self, dinh):
        pass

    def TongBanBacRa(self):
        pass

    def TongBanBacVao(self):
        pass

    def DayDu(self):
        pass

    def Vong(self):
        pass

    def HaiPhia(self):
        pass