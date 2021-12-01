import math

input_angle = float(input('角度を入力してください(度):'))
angle = input_angle * math.pi / 180

print(f"{input_angle} 度-> {angle}ラジアン")
print(f"sin({input_angle})=> {angle}")