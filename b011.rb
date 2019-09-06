#encoding:utf-8
#ruby 1.9.2

#入力文字列
input_lines = gets.split(' ').map(&:to_i)
N = input_lines[0]
M = input_lines[1]

page = (M.to_f / (N * 2)).ceil

result = 0
#ページ番号の半分以であれば表側
if(M <= ((page * N * 2) - N))
  first_pocket = (page - 1) * (N * 2) + 1 
  sub = M - first_pocket

  result = first_pocket + (N * 2) - 1 
  sub.times do |i|
    result -= 1
  end
else
  last_pocket = page * (N * 2)
  sub = last_pocket - M

  result = last_pocket - ((N * 2) - 1)
  sub.times do |i|
    result += 1
  end
end

puts result