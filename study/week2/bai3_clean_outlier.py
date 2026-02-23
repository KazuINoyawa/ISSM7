import pandas as pd
df = pd.read_csv("hvac_simulated_week2.csv")
# Cố tình chèn vài outlier
df.loc[5, "T_in"] = 99
df.loc[10, "T_in"] = -5
df.loc[20, "humidity"] = 0
df.loc[25, "humidity"] = 150
df.to_csv("hvac_with_outlier.csv", index=False)
print("Đã tạo hvac_with_outlier.csv với outlier.")

import pandas as pd
df = pd.read_csv("hvac_with_outlier.csv")
def is_T_in_bad(x):
    return x < 15 or x > 45
def is_humidity_bad(x):
    return x < 10 or x > 100
bad_T = df["T_in"].apply(is_T_in_bad)
bad_H = df["humidity"].apply(is_humidity_bad)
print("Số dòng T_in bất thường:", bad_T.sum())
print("Số dòng humidity bất thường:", bad_H.sum())
# Cách xử lý: thay bằng trung bình của 2 hàng lân cận (nếu có)
for idx in df[bad_T].index:
    if 1 <= idx < len(df) - 1:
        df.loc[idx, "T_in"] = (df.loc[idx - 1, "T_in"] +
df.loc[idx + 1, "T_in"]) / 2
    else:
        df.loc[idx, "T_in"] = df["T_in"].median()
for idx in df[bad_H].index:
    if 1 <= idx < len(df) - 1:
        df.loc[idx, "humidity"] = (df.loc[idx - 1, "humidity"] +
df.loc[idx + 1, "humidity"]) / 2

    else:
        df.loc[idx, "humidity"] = df["humidity"].median()
df.to_csv("hvac_cleaned.csv", index=False)
print("Đã lưu file hvac_cleaned.csv sau khi làm sạch.")