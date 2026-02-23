count_off = 0
count_medium = 0
count_high = 0

for step in range(1, 6):
    print(f"\n--- Bước {step} ---")
    T_in = float(input("Nhập nhiệt độ trong phòng (°C): "))
    n_people = int(input("Nhập số người trong phòng: "))
    if T_in > 29 or n_people > 30:
        decision = "AC HIGH"
        count_high += 1
    elif T_in > 26 or n_people > 20:
        decision = "AC MEDIUM"
        count_medium += 1
    else:
        decision = "AC OFF"
        count_off += 1

    print(f"Buoc {step}: T_in={T_in}, n_people={n_people}, Quyết định={decision}")
print("\n--- TỔNG KẾT ---")
print(f"Số lần AC OFF: {count_off}")
print(f"Số lần AC MEDIUM: {count_medium}")
print(f"Số lần AC HIGH: {count_high}")
