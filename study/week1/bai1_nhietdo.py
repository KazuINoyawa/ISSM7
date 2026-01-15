print("Nhập nhiệt độ trong phòng (*C): ")
temp = float(input())
if temp < 22:
    print("Nhiệt độ trong phòng lạnh.")
elif temp >= 22 and temp < 27:
    print("Nhiệt độ trong phòng vừa.")
else:
    print("Nhiệt độ trong phòng nóng.")