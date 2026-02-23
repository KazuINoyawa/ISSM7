T_in = float(input("Nhập nhiệt độ trong phòng (°C): "))
T_out = float(input("Nhập nhiệt độ ngoài trời (°C): "))
n_people = int(input("Nhập số người trong phòng: "))
capacity = 30  # đơn vị %
if T_out > 35:
    capacity += 20

if n_people > 30:
    capacity += 20

if T_in > 28:
    capacity += 20

if capacity > 100:
    capacity = 100
print(f"Công suất điều hòa cần thiết là: {capacity}%")
