import matplotlib.pyplot as plt
def rule_ac_power(T_in, occ_level):
    if T_in > 30 and occ_level >= 1:
        return 80, 3
    elif 27 <= T_in <= 30:
        return 50, 2
    else:
        return 20, 1
T_in = 29.0
T_out = 32.0
occ_level = 2
T_in_list = []
ac_list = []
for step in range(60): # 60 bước
    if step < 20:
        occ_level = 2
    elif step < 40:
        occ_level = 1
    else:
        occ_level = 0
    ac_power, fan_level = rule_ac_power(T_in, occ_level)
    dT = 0.0
    if ac_power >= 70:
        dT -= 0.15
    elif ac_power >= 40:
        dT -= 0.08
    else:
        dT -= 0.02
    if T_out >= 31:
        dT += 0.10
    if occ_level == 2:
        dT += 0.08
    elif occ_level == 1:
        dT += 0.04
    T_in += dT
    if T_in < 20:
        T_in = 20
    if T_in > 35:
        T_in = 35
    T_in_list.append(T_in)
    ac_list.append(ac_power)
plt.figure(figsize=(10,4))
plt.plot(T_in_list, label="T_in")
plt.xlabel("Step")
plt.ylabel("T_in (°C)")
plt.title("Mô phỏng T_in theo bước với luật cứng")
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(10,3))
plt.step(range(len(ac_list)), ac_list, where="post")
plt.xlabel("Step")
plt.ylabel("ac_power (%)")
plt.title("Công suất AC theo bước")
plt.tight_layout()
plt.show()