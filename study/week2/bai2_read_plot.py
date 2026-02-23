import pandas as pd
import matplotlib.pyplot as plt
# Đọc file CSV
df = pd.read_csv("hvac_simulated_week2.csv")
print(df.head())
# Chuyển timestamp thành kiểu datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])
# Vẽ T_in và T_out
plt.figure(figsize=(10, 4))
plt.plot(df["timestamp"], df["T_in"], label="T_in")
plt.plot(df["timestamp"], df["T_out"], label="T_out")
plt.xlabel("Thời gian")
plt.ylabel("Nhiệt độ (°C)")
plt.title("Nhiệt độ trong/ngoài theo thời gian")
plt.legend()
plt.tight_layout()
plt.show()
# Vẽ occ_level
plt.figure(figsize=(10, 3))
plt.step(df["timestamp"], df["occ_level"], where="post")
plt.xlabel("Thời gian")
plt.ylabel("occ_level")
plt.title("Mức occupancy theo thời gian")
plt.tight_layout()
plt.show()