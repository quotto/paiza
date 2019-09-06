# ruby-1.9.3
# coding:utf-8

include Math

# 重力加速度
g = 9.8

input_lines = gets.split(' ').map(&:to_f)
# 初期の高さ
o_y = input_lines[0]
# 初速
s = input_lines[1]
# 角度
deg = input_lines[2]

# ラジアン
rad = (deg / 180) * PI

input_lines = gets.split(' ').map(&:to_f)
# 的までの横距離
x = input_lines[0]
# 的の高さ
y = input_lines[1]
# 的の直径
a = input_lines[1]

# 的の最高値
high = y + a * 0.5
# 的の最低値
low = y - a * 0.5

# 矢の当たる高さ
result = o_y + (x * tan(rad)) - (g * (x**2))/(2 * (s**2) * (cos(rad)**2))

# 的の中心からの距離
distance = -1.0
if result <= high and result >= y
  # 的の中心から上に命中した場合
  distance = result - y
elsif result >= low   and result < y
  # 的の中心よりも下に命中した場合
  distance = y - result 
end

if distance >= 0
  puts sprintf "Hit %.1f", distance 
else
  puts 'Miss'
end
