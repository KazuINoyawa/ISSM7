import pandas as pd
df = pd.read_csv("hvac_cleaned.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)
T_in_mean_all = df["T_in"].mean()
morning = df.between_time("07:00", "11:00")
noon = df.between_time("11:00", "13:00")
afternoon = df.between_time("13:00", "17:00")
print("T_in trung bình cả ngày:", round(T_in_mean_all, 2))
print("T_in trung bình buổi sáng:",
round(morning['T_in'].mean(), 2))
print("T_in trung bình buổi trưa:",
round(noon['T_in'].mean(), 2))
print("T_in trung bình buổi chiều:",
round(afternoon['T_in'].mean(), 2))
mask_hot = df["T_in"] > 30
mask_comfort = (df["T_in"] >= 24) & (df["T_in"] <= 27)
minutes_per_step = 5
hot_minutes = mask_hot.sum() * minutes_per_step
comfort_minutes = mask_comfort.sum() * minutes_per_step
print("Số phút T_in > 30°C:", hot_minutes)
print("Số phút T_in trong °C:", comfort_minutes)