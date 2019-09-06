# ruby-1.9.3
# coding:utf-8

# 検索するアドレスを配列に分割
address_pattern = gets.split('.')

max_range = Array.new(4).map(){0}
min_range = Array.new(4).map(){0}
# 第3,4オクテットが*であれば範囲指定の記法に変更
2.upto(3) do |i|
  address_range = address_pattern[i].chomp
  if address_range == '*'
    address_range = '[0-255]'
  end
  if /(\d+)-(\d+)/ === address_range
    min_range[i] = $1.to_i
    max_range[i] = $2.to_i
  else
    max_range[i] = min_range[i] = address_range.to_i
  end
end

# 入力行
N = gets.to_i

# 結果格納用
result_table = Array.new

N.times do |n|
  input_lines = gets.split(' ')
  address_values = input_lines[0].split('.')
  if address_values[0] == address_pattern[0] and address_values[1] == address_pattern[1] and
    (address_values[2].to_i >= min_range[2] and address_values[2].to_i <= max_range[2]) and
    (address_values[3].to_i >= min_range[3] and address_values[3].to_i <= max_range[3]) 

    access_date = input_lines[3]
    access_date = access_date[1..access_date.length-1]
    view_page = input_lines[6]

    result_table.push("#{input_lines[0]} #{access_date} #{view_page}")
  end
end

puts result_table