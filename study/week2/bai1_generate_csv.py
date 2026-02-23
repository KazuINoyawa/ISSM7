import csv
from datetime import datetime, timedelta
from operator import gt
from turtle import lt

start_time = datetime(2025, 1, 1, 7, 0)
end_time = datetime(2025, 1, 1, 21, 0)
delta = timedelta(minutes=5)
def get_occ_level(t):
 h = t.hour
 if 7 <= h < 11:
  return 2
 elif 11 <= h < 13:
  return 1
 elif 13 <= h < 17:
  return 2
 else:
  return 0
def get_T_out(t):
 h = t.hour
 if 11 <= h < 14:
  return 33.0
 elif 9 <= h < 11 or 14 <= h < 16:
  return 31.0
 elif 7 <= h < 9 or 16 <= h < 18:
  return 29.0
 else:
  return 27.0
def rule_ac_power(T_in, occ_level):
 if T_in > 30 and occ_level >= 1:
  return 80, 3
 elif 27 <= T_in <= 30:
  return 50, 2
 else:
  return 20, 1
# Khởi tạo
rows = []
T_in = 28.0
humidity = 75.0

current_time = start_time
while current_time <= end_time:
 T_out = get_T_out(current_time)
 occ_level = get_occ_level(current_time)
 ac_power, fan_level = rule_ac_power(T_in, occ_level)
# Mô hình rất đơn giản cho T_in
# AC càng mạnh -> T_in giảm
# Nắng + đông người -> T_in tăng
 dT = 0.0
# ảnh hưởng AC
 if ac_power > 70:
    dT -= 0.15
# ảnh hưởng T_out
 elif ac_power >= 40:
    dT -= 0.08
 else:
    dT -= 0.02
# ảnh hưởng T_out và occupancy
 if T_out >= 31:
    dT += 0.10
 if occ_level == 2:
    dT += 0.08
 elif occ_level == 1:
    dT += 0.04
 T_in = T_in + dT
# giữ T_in trong khoảng hợp lý
 if T_in < 20:
    T_in = 20
 if T_in > 35:
    T_in = 35
 row = {"timestamp": current_time.strftime("%Y-%m-%d %H:%M"),
"T_in": round(T_in, 2),
"T_out": round(T_out, 2),
"humidity": round(humidity, 1),
"occ_level": occ_level,
"ac_power": ac_power,
"fan_level": fan_level
}
 rows.append(row)
 current_time += delta
# Ghi ra CSV
with open("hvac_simulated_week2.csv", mode="w",
        newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["timestamp", "T_in", "T_out",
        "humidity", "occ_level", "ac_power", "fan_level"]
        )
    writer.writeheader()
    writer.writerows(rows)
print("Đã tạo file hvac_simulated_week2.csv với",
len(rows), "dòng.")