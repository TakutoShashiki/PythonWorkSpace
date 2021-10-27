# 【実行例】
# > python math.py
# 角度を入力してください（度）：45
# 45.0 度->0.7853981633974483 ラジアン
# sin(45.0)=>0.7071067811865475


# 【math.py】
import math
input_angle = float(input('角度を入力してください（度）：'))
angle = input_angle * math.pi / 180

print(f"{input_angle} 度-> {angle}ラジアン")
print(f"sin({input_angle})=> {angle}")