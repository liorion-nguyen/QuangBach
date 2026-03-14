import random

def doan_so(so_lan_doan, so_bi_mat) :
    for i in range(1, so_lan_doan + 1):
        if so_lan_doan - i < 2:
            print(f"Ban con {so_lan_doan - i} luot doan!")
        so_doan = int(input(f"Lan {i}: doan so nao?"))
        if so_doan < so_bi_mat:
            print(" so ban doan nhỏ hon so bi mat")
        elif so_doan > so_bi_mat:
            print(" so ban doan lon hon so bi mat")
        else:
            print(f" chúc mung ban da doan dung, so bi mat la {so_bi_mat}")
            break
    else:
        print(f"het luot doan! so bi mat la {so_bi_mat}")
def main():
    while True:
        print("======TRO CHOI DOAN SO======")
        while True:
            print("nhap vao muc_do")
            print("1.(1-50) có 7 lượt đoán")
            print("2. (1-100) có 6 luot doan")
            print("3. (1-200) có 5 luot doan")
            muc_do = int(input("chon muc do"))
            if muc_do == 1:
                so_lan_doan = 7
                so_bi_mat = random.randint(1,50)
            elif muc_do == 2:
                so_lan_doan = 6
                so_bi_mat = random.randint(1,100)
            elif muc_do == 3:
                so_lan_doan = 5
                so_bi_mat = random.randint(1,200)
            else:
                print("muc do k hop le")
                continue
            break
        if muc_do == 1:
            print(" toi da nghi ra 1 so tu 1 den 50)")
        elif muc_do == 2:
            print(" toi da nghi ra 1 so tt 1 den 100")
        elif muc_do == 3:
            print(" toi da nghi ra 1 so tu 1 den 200")
        doan_so(so_lan_doan, so_bi_mat)

        choi_lai = input("ban co muon chs lai? (y/n):")
        if choi_lai.lower() != "y":
            break
   
main()