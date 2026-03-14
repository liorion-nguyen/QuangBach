import math

def nhap_so():
    while True:
        try:
            return float(input("👉 Nhập số: "))
        except:
            print("❌ Vui lòng nhập số hợp lệ!")

def may_tinh():
    while True:
        print("\n" + "="*35)
        print("🧮        MÁY TÍNH CƠ BẢN")
        print("="*35)

        print("1️⃣  Cộng (+)")
        print("2️⃣  Trừ (-)")
        print("3️⃣  Nhân (×)")
        print("4️⃣  Chia (÷)")
        print("5️⃣  Lũy thừa (a^b)")
        print("6️⃣  Căn bậc hai (√a)")
        print("0️⃣  Thoát")

        try:
            chon = int(input("\n👉 Chọn phép tính: "))
        except:
            print("❌ Nhập sai định dạng!")
            continue

        if chon == 0:
            print("👋 Tạm biệt!")
            break

        elif chon in [1,2,3,4,5]:
            a = nhap_so()
            b = nhap_so()

            if chon == 1:
                print(f"✅ Kết quả: {a} + {b} = {a+b}")

            elif chon == 2:
                print(f"✅ Kết quả: {a} - {b} = {a-b}")

            elif chon == 3:
                print(f"✅ Kết quả: {a} × {b} = {a*b}")

            elif chon == 4:
                if b == 0:
                    print("❌ Không thể chia cho 0")
                else:
                    print(f"✅ Kết quả: {a} ÷ {b} = {a/b}")

            elif chon == 5:
                print(f"✅ Kết quả: {a}^{b} = {a**b}")

        elif chon == 6:
            a = nhap_so()
            if a < 0:
                print("❌ Không thể căn số âm")
            else:
                print(f"✅ √{a} = {math.sqrt(a)}")

        else:
            print("❌ Lựa chọn không hợp lệ!")

may_tinh()